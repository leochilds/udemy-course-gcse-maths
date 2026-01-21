#!/bin/bash

# Simple wrapper script to render Manim animations
# Usage: ./render_animation.sh <path_to_animation_file> [quality] [scene_name]

FILE_PATH=$1
QUALITY=${2:-l} # Default to low quality (480p15)
SCENE_NAME=$3

# Determine Manim executable
if [ -f ".venv/bin/manim" ]; then
    MANIM_CMD=".venv/bin/manim"
else
    MANIM_CMD="manim"
fi

if [ -z "$FILE_PATH" ]; then
    echo "Usage: ./render_animation.sh <path_to_animation_file> [quality] [scene_name]"
    echo ""
    echo "Arguments:"
    echo "  <path_to_animation_file>  Path to the python animation script"
    echo "  [quality]                 Optional. l=low (480p), m=medium (720p), h=high (1080p). Default: l"
    echo "  [scene_name]              Optional. Specific scene to render. If omitted, Manim may prompt or render all."
    echo ""
    echo "Example:"
    echo "  ./render_animation.sh animations/section-01/lesson-01.1-animation-01.py m"
    exit 1
fi

# Validate quality
if [[ ! "$QUALITY" =~ ^(l|m|h|p|k)$ ]]; then
    echo "Warning: Quality '$QUALITY' is not one of standard codes (l, m, h, p, k). Manim might fail."
fi

echo "Rendering $FILE_PATH at quality '$QUALITY' using $MANIM_CMD..."

if [ -z "$SCENE_NAME" ]; then
    $MANIM_CMD -q "$QUALITY" "$FILE_PATH"
else
    $MANIM_CMD -q "$QUALITY" "$FILE_PATH" "$SCENE_NAME"
fi
