# Animations Folder

This folder contains Manim animation scripts used to create visual learning materials for the GCSE Maths Course.

## About Manim

Manim is a mathematical animation engine created by Grant Sanderson (3Blue1Brown). It's used to create precise, programmatic animations that are particularly well-suited for mathematical concepts.

- **Official Documentation**: https://docs.manim.community/
- **Installation Guide**: https://docs.manim.community/en/stable/installation.html

## Structure

Animations are organized by section:

```
animations/
├── section-01-[name]/
│   ├── lesson-XX-animation-01.py
│   ├── lesson-XX-animation-02.py
│   └── ...
├── section-02-[name]/
└── ...
```

## Naming Convention

Format: `lesson-XX-animation-YY.py`

- `XX`: Lesson number (matches the lesson file)
- `YY`: Animation number within that lesson (01, 02, 03...)

Example: `lesson-03-animation-01.py` would be the first animation for lesson 3.

## Narration Guidelines

To ensure correct pronunciation by the AI voiceover, always write numbers as whole words in the narration text.

- Decimals: `3.42` -> "three point four two"
- Integers: `342` -> "three hundred and forty-two"
- Money: `£36.67` -> "thirty-six pounds sixty-seven"

## Creating Animations

### Installation

First, install Manim Community Edition:

```bash
# On Ubuntu/Debian
sudo apt update
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg
pip install manim

# On macOS
brew install py3cairo ffmpeg
pip install manim

# On Windows
# Follow the detailed instructions at: https://docs.manim.community/en/stable/installation/windows.html
```

### Basic Animation Template

```python
from manim import *

class MyAnimation(Scene):
    def construct(self):
        # Your animation code here
        text = Text("Hello, GCSE Maths!")
        self.play(Write(text))
        self.wait(2)
```

### Rendering Animations

To render an animation:

```bash
# High quality (1080p, 60fps) - for final production
manim -pqh lesson-XX-animation-YY.py MyAnimation

# Medium quality - for preview
manim -pqm lesson-XX-animation-YY.py MyAnimation

# Low quality - for quick testing
manim -pql lesson-XX-animation-YY.py MyAnimation
```

Flags:
- `-p`: Preview (automatically play after rendering)
- `-q`: Quality (h=high, m=medium, l=low)

### Helper Script

A helper script `render_animation.sh` is provided in the root directory to simplify rendering.

Usage:
```bash
./render_animation.sh <path_to_file> [quality] [scene_name]
```

Examples:
```bash
# Render low quality (default)
./render_animation.sh animations/section-01/lesson-01.1-animation-01.py

# Render medium quality
./render_animation.sh animations/section-01/lesson-01.1-animation-01.py m

# Render specific scene at high quality
./render_animation.sh animations/section-01/lesson-01.1-animation-01.py h ColumnMultiplication
```

### Output Location

Rendered videos are saved in `media/videos/[filename]/[quality]/`

## Guidelines for Mathematical Animations

### When to Create Animations

**ONLY create animations when motion/transformation adds clear pedagogical value:**

✅ **Good use cases:**
- Geometric transformations (rotations, reflections, translations)
- Graph plotting/building step by step
- Morphing equations to show equivalence
- Visualizing Pythagoras' theorem
- Demonstrating trigonometric functions on unit circle
- Showing area under curves
- Animated number line operations

❌ **Poor use cases:**
- Static diagrams (use images instead)
- Simple text reveals (use PowerPoint transitions)
- Decorative effects without learning value
- Content that doesn't benefit from motion

### Animation Principles

1. **Keep it simple**: Avoid over-animation
2. **Clear and slow**: Learners need time to process
3. **Focus on one concept**: Don't cram multiple ideas
4. **Use consistent styling**: Maintain visual coherence across animations
5. **Consider production time**: Balance quality with time investment

### Recommended Timing

- **Pause before key moments**: Give learners time to anticipate
- **Slow down important steps**: Let complex transformations be visible
- **Add wait times**: Use `self.wait(1)` or `self.wait(2)` appropriately
- **Typical animation length**: 10-60 seconds per concept

## Common Manim Patterns for Maths

### Coordinate System

```python
axes = Axes(
    x_range=[-5, 5, 1],
    y_range=[-5, 5, 1],
    axis_config={"include_tip": True}
)
labels = axes.get_axis_labels(x_label="x", y_label="y")
self.play(Create(axes), Write(labels))
```

### Plotting a Function

```python
graph = axes.plot(lambda x: x**2, color=BLUE)
self.play(Create(graph))
```

### Geometric Shapes

```python
triangle = Polygon([0, 0, 0], [2, 0, 0], [1, 2, 0], color=BLUE)
self.play(Create(triangle))
```

### Mathematical Equations

```python
equation = MathTex(r"a^2 + b^2 = c^2")
self.play(Write(equation))
```

### Transforming Equations

```python
eq1 = MathTex("2x", "+", "3", "=", "7")
eq2 = MathTex("2x", "=", "7", "-", "3")
eq3 = MathTex("2x", "=", "4")

self.play(Write(eq1))
self.wait(1)
self.play(TransformMatchingTex(eq1, eq2))
self.wait(1)
self.play(TransformMatchingTex(eq2, eq3))
```

## Resources

### Learning Manim
- **Official Tutorial**: https://docs.manim.community/en/stable/tutorials.html
- **Example Gallery**: https://docs.manim.community/en/stable/examples.html
- **3Blue1Brown Videos**: Study Grant's videos to see excellent mathematical animation

### Branding & Color Scheme

**Target Audience:** Adult Learners (Resitters, Career Changers).
**Style:** Professional, Clean, Minimal Distractions, High Contrast (Dark Mode).

The course uses a strict color palette defined in `animations/styles.py`. All animations **must** import and use these colors.

| Role | Color | Hex Code | Usage |
|------|-------|----------|-------|
| **Background** | Deep Navy | `#0B0F19` | Scene background (Standard Slide Color) |
| **Text** | White | `#FFFFFF` | Primary numbers, text, equations |
| **Active** | Light Blue | `#29B6F6` | Currently active numbers, focus elements, cursors |
| **Carry/Action** | Coral | `#FF7043` | Carry digits, bullets, distinct actions |
| **Answer** | Soft Gold | `#FFD54F` | Final answers, key results |
| **Auxiliary** | Blue Grey | `#90A4AE` | Side calculations, notes, secondary info |

#### Usage Example

```python
from animations.styles import Brand

class MyScene(Scene):
    def construct(self):
        Brand.set_default_theme(self) # Sets background and default text color
        
        # Use Brand constants
        eq = MathTex("2x = 10").set_color(Brand.TEXT)
        self.play(Indicate(eq, color=Brand.ACTIVE))
```

## Exporting for PowerPoint

Once rendered, animations can be:
1. Embedded directly in PowerPoint slides
2. Converted to GIF if needed for compatibility
3. Saved as high-quality MP4 for best results

### Converting to GIF (if needed)

```bash
ffmpeg -i animation.mp4 -vf "fps=30,scale=720:-1:flags=lanczos" animation.gif
```

## Tips

1. **Test frequently**: Render at low quality while developing
2. **Comment your code**: Explain what each section does
3. **Version control**: Commit working animations before major changes
4. **Reusable components**: Create helper functions for repeated patterns
5. **Performance**: Complex scenes can take time to render - optimize when possible

---

For questions or issues with Manim, consult the official documentation or community forums.
