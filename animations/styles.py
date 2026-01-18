from manim import *

class Brand:
    """
    Central branding configuration for GCSE Maths Course.
    Target Audience: Adult Learners (Professional, Clean, High Contrast)
    """
    
    # --- Color Palette ---
    BACKGROUND = "#0B0F19" # Deep Navy/Black
    TEXT = "#FFFFFF"       # White
    
    # Functional Colors
    ACTIVE = "#29B6F6"     # Light Blue - For current focus/action
    CARRY = "#FF7043"      # Coral - For carry digits (distinct but not aggressive red)
    ANSWER = "#FFD54F"     # Soft Gold - For final results
    AUXILIARY = "#90A4AE"  # Blue Grey - For side calculations/notes

    @classmethod
    def set_default_theme(cls, scene):
        """Applies the brand theme to the scene."""
        scene.camera.background_color = cls.BACKGROUND
        Text.set_default(color=cls.TEXT)
        MathTex.set_default(color=cls.TEXT)
        # Ensure lines and other Mobjects default to a visible color if needed, 
        # though Manim defaults are usually fine if background is dark.
