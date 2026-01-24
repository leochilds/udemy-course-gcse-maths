# AI Voice Tuning and Usage Guide

This guide explains how to fine-tune the VoxCPM model with your voice data and how to use the fine-tuned model in your Manim animations.

## 1. Retuning with New Voice Data

If you have recorded new voice clips and want to update the model or train a new one, follow these steps:

### Step 1: Add Data
1.  Place your new `.webm` audio files and corresponding `.txt` transcripts into the `voice_data/en-GB/` directory.
    - Ensure filenames match (e.g., `001.webm` and `001.txt`).
    - You can organize them in subdirectories; the processing script scans recursively.

### Step 2: Process Data
Run the data processing script to convert audio to the required format (WAV, 44.1kHz) and update the training manifest (`train.jsonl`).

```bash
.venv/bin/python process_voice_data.py
```

This will:
- Convert new `.webm` files to `.wav` in `processed_voice_data/`.
- Regenerate `train.jsonl` with all valid audio/text pairs found.

### Step 3: Run Fine-tuning
Execute the training script using the custom configuration file.

```bash
cd VoxCPM
../.venv/bin/python scripts/train_voxcpm_finetune.py --config_path conf/voxcpm_v1.5/voxcpm_finetune_myvoice.yaml
```

**Note:**
- This will start training for 2000 steps (default configuration).
- Checkpoints are saved to `checkpoints/myvoice/`.
- If you want to start fresh, you may want to delete `checkpoints/myvoice/` before running, or change the `save_path` in `VoxCPM/conf/voxcpm_v1.5/voxcpm_finetune_myvoice.yaml`.
- The latest checkpoint will be in `checkpoints/myvoice/step_0002000` (or the highest step number).

## 2. Using the Fine-tuned Voice in Manim

To use your custom AI voice in Manim animations, you need to use the `VoxCPMService`.

### Step 1: Import the Service
In your animation script (e.g., `lesson-01.0-introduction.py`), import the service:

```python
from animations.voxcpm_service import VoxCPMService
```

### Step 2: Configure the Service
In the `construct` method of your `VoiceoverScene`, replace `GTTSService` (or `AzureService`) with `VoxCPMService`. You must specify the path to your fine-tuned checkpoint and the base model.

```python
class MyLesson(VoiceoverScene):
    def construct(self):
        # ... setup ...
        
        self.set_speech_service(VoxCPMService(
            checkpoint_dir="/home/leo/code/udemy-course-gcse-maths/checkpoints/myvoice/step_0002000",
            base_model_path="/home/leo/code/udemy-course-gcse-maths/models/VoxCPM1.5"
        ))
        
        # ... your animation code ...
```

- **`checkpoint_dir`**: The path to the specific checkpoint directory (e.g., `.../step_0002000`) generated during training.
- **`base_model_path`**: The path to the downloaded VoxCPM base model.

### Step 3: Generate Voiceovers
Use the `self.voiceover()` context manager as usual. The service will automatically generate audio using your AI model.

```python
        with self.voiceover(text="Welcome to this lesson on quadratic equations.") as tracker:
            self.play(Write(Text("Quadratics")))
```

### Troubleshooting
- **Cache Issues**: If you change the model but don't see changes in the audio, try deleting `media/voiceovers/cache.json` to force regeneration.
- **Audio Format**: The service automatically handles conversion to MP3, which is required by Manim's current video assembly process.
