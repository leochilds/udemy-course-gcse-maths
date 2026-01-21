#!/bin/bash

# Ensure .env exists to avoid docker-compose warnings
if [ ! -f .env ]; then
    touch .env
fi

if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <command>"
    echo "Example: $0 python render_all.py"
    echo "Example: $0 ./render_animation.sh animations/section-01/lesson-01.1-animation-01.py"
    exit 1
fi

docker-compose run --rm renderer "$@"
