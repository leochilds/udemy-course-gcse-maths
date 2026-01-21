import argparse
import json
import os
import re
import sys
import subprocess
import threading
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# Try to import rich
try:
    from rich.console import Console
    from rich.progress import (
        Progress,
        SpinnerColumn,
        BarColumn,
        TextColumn,
        TimeRemainingColumn,
        TaskID,
    )
    from rich.live import Live
    from rich.panel import Panel
    from rich.console import Group
    from rich.layout import Layout
    from rich import box
except ImportError as e:
    print(f"Error importing rich: {e}")
    print("Error: 'rich' library is required. Please install it with 'pip install rich'.")
    sys.exit(1)

# Configuration
LOG_FILE = "render_log.json"
ANIMATIONS_DIR = "animations"
# Manim quality mapping
QUALITY_MAP = {
    'l': '480p15',
    'm': '720p30',
    'h': '1080p60',
    'p': '1440p60',
    'k': '2160p60',
}

class RenderManager:
    def __init__(self, quality, jobs, skip_existing):
        self.quality = quality
        self.quality_dir = QUALITY_MAP.get(quality, 'unknown')
        self.jobs = jobs
        self.skip_existing = skip_existing
        self.console = Console()
        self.lock = threading.RLock()
        self.manim_cmd = self.determine_manim_cmd()
        
        # State
        self.completed_files = set()
        self.files_to_render = []
        self.skipped_files = []
        self.failed_files = []
        
        self.load_state()

    def get_animation_files(self):
        """Recursively find valid animation files."""
        files = []
        for root, _, filenames in os.walk(ANIMATIONS_DIR):
            for filename in filenames:
                if filename.endswith(".py") and filename not in ["__init__.py", "styles.py"]:
                    path = os.path.join(root, filename)
                    # Simple check if file contains a Scene class
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if re.search(r'class\s+\w+\(.*Scene\):', content):
                            files.append(path)
        return sorted(files)

    def get_scenes_in_file(self, filepath):
        """Extract scene class names from a file."""
        scenes = []
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Matches: class MyScene(Scene): or class MyScene(MovingCameraScene):
            matches = re.findall(r'class\s+(\w+)\(.*Scene\):', content)
            scenes.extend(matches)
        return scenes

    def get_output_path(self, filepath, scene_name):
        """Determine expected output path for a scene."""
        # Standard Manim output: media/videos/{module_name}/{quality}/{scene_name}.mp4
        # module_name is filename without extension
        module_name = Path(filepath).stem
        return Path("media") / "videos" / module_name / self.quality_dir / f"{scene_name}.mp4"

    def determine_manim_cmd(self):
        """Detect correct manim executable."""
        if os.path.exists(".venv/bin/manim"):
            return ".venv/bin/manim"
        return "manim"

    def load_state(self):
        """Load render log for resumability."""
        if os.path.exists(LOG_FILE):
            try:
                with open(LOG_FILE, 'r') as f:
                    data = json.load(f)
                    # Check if previous run was completed
                    if data.get('status') == 'completed':
                        # Start fresh
                        self.completed_files = set()
                    else:
                        # Resume
                        self.completed_files = set(data.get('completed', []))
            except Exception as e:
                self.console.print(f"[yellow]Warning: Could not load log file: {e}[/yellow]")
                self.completed_files = set()
        else:
            self.completed_files = set()

    def save_state(self, status="in_progress"):
        """Save current progress to log."""
        # print(f"Saving state: {status} with {len(self.completed_files)} files")
        try:
            with self.lock:
                data = {
                    "last_update": datetime.now().isoformat(),
                    "status": status,
                    "completed": list(self.completed_files)
                }
                with open(LOG_FILE, 'w') as f:
                    json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving state: {e}")

    def mark_completed(self, filepath):
        with self.lock:
            self.completed_files.add(filepath)
            self.save_state()

    def check_if_should_skip(self, filepath):
        """Check if file should be skipped based on --skip-existing."""
        if not self.skip_existing:
            return False
        
        scenes = self.get_scenes_in_file(filepath)
        if not scenes:
            return False # Can't determine, so don't skip
            
        all_exist = True
        for scene in scenes:
            out_path = self.get_output_path(filepath, scene)
            if not out_path.exists():
                all_exist = False
                break
        
        return all_exist

    def run(self):
        all_files = self.get_animation_files()
        
        # Filter out already completed files (from resumable log)
        files_queue = [f for f in all_files if f not in self.completed_files]
        
        if not files_queue and len(all_files) > 0:
            # If all files are in completed_files, it means we probably want to start over
            # unless the log was explicit. But load_state logic handles 'completed' status.
            # If we are here, it means 'in_progress' but all files done.
            # Let's just finish.
            self.save_state("completed")
            self.console.print("[green]All files already marked as completed in current run.[/green]")
            return

        # Setup Rich Progress
        overall_progress = Progress(
            TextColumn("[bold blue]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            "{task.completed}/{task.total}",
            TimeRemainingColumn(),
        )
        
        overall_task = overall_progress.add_task("Total Progress", total=len(files_queue))
        
        # Worker progress bars (one per job)
        worker_progress = Progress(
            TextColumn("[bold green]{task.fields[filename]}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TextColumn("{task.fields[status]}"),
        )
        
        # Create a task for each worker slot
        worker_tasks = []
        for i in range(self.jobs):
            tid = worker_progress.add_task(f"Worker {i+1}", filename="Waiting...", status="Idle", visible=False)
            worker_tasks.append(tid)

        # Thread-safe queue or list popping
        queue_lock = threading.Lock()
        current_index = 0

        def get_next_file():
            nonlocal current_index
            with queue_lock:
                if current_index < len(files_queue):
                    f = files_queue[current_index]
                    current_index += 1
                    return f
                return None

        def worker_func(worker_id):
            task_id = worker_tasks[worker_id]
            while True:
                filepath = get_next_file()
                if filepath is None:
                    break
                
                filename = os.path.basename(filepath)
                worker_progress.update(task_id, visible=True, filename=filename, total=100, completed=0, status="Starting...")
                
                # Check skip-existing
                if self.check_if_should_skip(filepath):
                    worker_progress.update(task_id, completed=100, status="Skipped (Exists)")
                    self.mark_completed(filepath)
                    with self.lock:
                        self.skipped_files.append(filepath)
                    overall_progress.advance(overall_task)
                    time.sleep(0.5) # Brief pause to let user see it skipped
                    continue

                # Run Manim
                cmd = [self.manim_cmd, "-q" + self.quality, filepath, "-a", "--disable_caching"]
                
                # Buffer for error logging
                output_buffer = []

                try:
                    process = subprocess.Popen(
                        cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        universal_newlines=True,
                        bufsize=1
                    )
                    
                    for line in process.stdout:
                        output_buffer.append(line)

                        # Try to find percentage with optional description
                        match = re.search(r'(?:(.+?):\s+)?(\d+)%\|', line)
                        if match:
                            desc = match.group(1)
                            percent = int(match.group(2))
                            
                            update_kwargs = {"completed": percent}
                            if desc:
                                update_kwargs["status"] = f"Rendering {desc.strip()}"
                            
                            worker_progress.update(task_id, **update_kwargs)
                            
                        elif "Rendering" in line:
                            # Try to extract specific scene/animation name
                            match_render = re.search(r'Rendering\s+(.*?)\.\.\.', line)
                            if match_render:
                                worker_progress.update(task_id, status=f"Rendering {match_render.group(1).strip()}")
                            else:
                                worker_progress.update(task_id, status="Rendering Scene")

                    process.wait()
                    
                    if process.returncode == 0:
                        worker_progress.update(task_id, completed=100, status="Done")
                        self.mark_completed(filepath)
                    else:
                        worker_progress.update(task_id, status="[red]Failed[/red]")
                        with self.lock:
                            self.failed_files.append(filepath)
                            with open("render_errors.log", "a") as err_log:
                                err_log.write(f"--- Failure in {filename} ---\n")
                                err_log.write("".join(output_buffer))
                                err_log.write("\n" + "="*40 + "\n")
                            
                except Exception as e:
                    worker_progress.update(task_id, status=f"[red]Error: {str(e)}[/red]")
                    with self.lock:
                        self.failed_files.append(filepath)
                        with open("render_errors.log", "a") as err_log:
                            err_log.write(f"--- Exception in {filename} ---\n")
                            err_log.write(str(e))
                            err_log.write("\n" + "="*40 + "\n")
                
                overall_progress.advance(overall_task)

            # Worker done
            worker_progress.update(task_id, visible=False)

        # UI Layout
        layout = Group(
            Panel(overall_progress, title="Overall Progress", border_style="blue"),
            Panel(worker_progress, title="Active Renders", border_style="green")
        )

        with Live(layout, console=self.console, refresh_per_second=10):
            with ThreadPoolExecutor(max_workers=self.jobs) as executor:
                futures = [executor.submit(worker_func, i) for i in range(self.jobs)]
                for future in futures:
                    future.result()

        # Final Summary
        self.console.print("\n[bold]Render Run Completed[/bold]")
        self.console.print(f"Total Files: {len(files_queue)}")
        self.console.print(f"Skipped: {len(self.skipped_files)}")
        self.console.print(f"Failed: {len(self.failed_files)}")
        
        if self.failed_files:
            self.console.print("[red]Failed Files:[/red]")
            for f in self.failed_files:
                self.console.print(f"  - {f}")
        
        if not self.failed_files and len(files_queue) > 0:
            self.save_state("completed")
            self.console.print("[green]Run marked as complete.[/green]")

def main():
    parser = argparse.ArgumentParser(description="Render all Manim animations in the project.")
    parser.add_argument("quality", choices=['l', 'm', 'h', 'p', 'k'], default='l', nargs='?', help="Render quality (default: l)")
    parser.add_argument("--jobs", "-j", type=int, default=2, help="Number of parallel jobs (default: 2)")
    parser.add_argument("--skip-existing", "-s", action="store_true", help="Skip rendering if output video exists")
    
    args = parser.parse_args()
    
    manager = RenderManager(args.quality, args.jobs, args.skip_existing)
    manager.run()

if __name__ == "__main__":
    main()
