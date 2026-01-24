import os
import json
import subprocess
from pathlib import Path
from tqdm import tqdm

SOURCE_DIR = Path("voice_data/en-GB").resolve()
OUTPUT_DIR = Path("processed_voice_data").resolve()
MANIFEST_FILE = Path("train.jsonl").resolve()

def process_data():
    if not SOURCE_DIR.exists():
        print(f"Source directory {SOURCE_DIR} does not exist.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    entries = []
    
    # Find all webm files
    webm_files = list(SOURCE_DIR.rglob("*.webm"))
    print(f"Found {len(webm_files)} audio files.")
    
    for webm_path in tqdm(webm_files, desc="Processing files"):
        # Check for corresponding text file
        txt_path = webm_path.with_suffix(".txt")
        if not txt_path.exists():
            print(f"Warning: No text file for {webm_path}")
            continue
            
        # Read text
        try:
            with open(txt_path, "r", encoding="utf-8") as f:
                text = f.read().strip()
        except Exception as e:
            print(f"Error reading {txt_path}: {e}")
            continue
            
        if not text:
            print(f"Warning: Empty text file {txt_path}")
            continue

        # Prepare output wav path
        # Maintain directory structure relative to SOURCE_DIR
        rel_path = webm_path.relative_to(SOURCE_DIR)
        wav_path = OUTPUT_DIR / rel_path.with_suffix(".wav")
        
        # Ensure parent directory exists
        wav_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Convert to WAV
        if not wav_path.exists():
            try:
                subprocess.run([
                    "ffmpeg", "-y", "-i", str(webm_path),
                    "-ar", "44100", "-ac", "1",  # 44.1kHz, Mono
                    str(wav_path)
                ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                print(f"Error converting {webm_path}: {e}")
                continue
        
        # Add to manifest
        entries.append({
            "audio": str(wav_path),
            "text": text
        })
        
    # Write manifest
    print(f"Writing {len(entries)} entries to {MANIFEST_FILE}...")
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry) + "\n")
            
    print("Data processing complete.")

if __name__ == "__main__":
    process_data()
