FROM manimcommunity/manim:v0.19.2

USER root

# Install system dependencies
# sox is required for some audio operations in manim-voiceover
RUN apt-get update && apt-get install -y --no-install-recommends \
    sox \
    libsox-fmt-mp3 \
    && rm -rf /var/lib/apt/lists/*

USER manimuser

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
