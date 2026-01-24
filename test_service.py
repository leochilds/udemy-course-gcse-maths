from animations.voxcpm_service import VoxCPMService
import os
import sys

# Ensure we can import animations
sys.path.append(os.getcwd())

service = VoxCPMService(
    checkpoint_dir="/home/leo/code/udemy-course-gcse-maths/checkpoints/myvoice/step_0002000",
    base_model_path="/home/leo/code/udemy-course-gcse-maths/models/VoxCPM1.5"
)

text = "Hello world"
output = service.generate_from_text(text, cache_dir=".", path="test_output.mp3")
print(output)

# Check if valid mp3
from mutagen.mp3 import MP3
try:
    audio = MP3("test_output.mp3")
    print(f"Duration: {audio.info.length}")
except Exception as e:
    print(f"Error reading MP3: {e}")
