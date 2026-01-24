import os
import json
import hashlib
import numpy as np
import soundfile as sf
from pydub import AudioSegment
from pathlib import Path
from manim_voiceover.services.base import SpeechService
from voxcpm.core import VoxCPM
from voxcpm.model.voxcpm import LoRAConfig

class VoxCPMService(SpeechService):
    def __init__(self, 
                 checkpoint_dir: str, 
                 base_model_path: str,
                 sample_rate: int = 44100,
                 **kwargs):
        super().__init__(**kwargs)
        self.checkpoint_dir = checkpoint_dir
        self.base_model_path = base_model_path
        self.sample_rate = sample_rate
        
        # Load config from checkpoint
        lora_config_path = os.path.join(checkpoint_dir, "lora_config.json")
        if os.path.exists(lora_config_path):
            with open(lora_config_path, "r") as f:
                lora_info = json.load(f)
            self.lora_config = LoRAConfig(**lora_info["lora_config"])
            print(f"Loaded LoRA config from {lora_config_path}")
        else:
            raise FileNotFoundError(f"LoRA config not found at {lora_config_path}")
        
        print("Loading VoxCPM model...")
        self.model = VoxCPM.from_pretrained(
            hf_model_id=base_model_path,
            lora_config=self.lora_config,
            lora_weights_path=checkpoint_dir,
            load_denoiser=False,
            optimize=True
        )
        print("VoxCPM model loaded.")

    def generate_from_text(self, text: str, cache_dir: str = None, path: str = None, **kwargs) -> dict:
        if cache_dir is None:
            cache_dir = self.cache_dir
        
        cache_dir = Path(cache_dir)
            
        input_data = {
            "input_text": text,
            "service": "VoxCPM",
            "checkpoint": self.checkpoint_dir
        }
        
        cached_result = self.get_cached_result(input_data, cache_dir)
        if cached_result is not None:
            return cached_result
            
        if path is None:
            basename = self.get_audio_basename(input_data)
            path = str(cache_dir / f"{basename}.mp3")

        print(f"Generating audio for: {text[:50]}...")
        print(f"Writing to: {path}")
        # Generate audio
        # Note: VoxCPM.generate returns a numpy array (1D float32)
        wav = self.model.generate(text=text)
        
        # Save to file (via temp wav then mp3)
        temp_wav = path.replace(".mp3", ".temp.wav")
        print(f"Temp wav: {temp_wav}")
        sf.write(temp_wav, wav, self.sample_rate)
        
        try:
            print("Exporting to MP3...")
            AudioSegment.from_wav(temp_wav).export(path, format="mp3")
            print("Export successful.")
        except Exception as e:
            print(f"Error exporting to MP3: {e}")
            raise
        
        if os.path.exists(temp_wav):
            os.remove(temp_wav)
        
        return {
            "original_audio": os.path.basename(path),
            "input_text": text,
            "input_data": input_data
        }
