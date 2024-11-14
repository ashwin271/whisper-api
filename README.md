# Whisper API

A FastAPI-based API for OpenAI's Whisper speech recognition model.

## Prerequisites

- Python 3.10+
- ffmpeg

## Setup

1. Install ffmpeg:
```bash
# Using the setup script
./scripts/setup_ffmpeg.sh

# Or manually:
# Ubuntu/Debian
sudo apt update && sudo apt install -y ffmpeg

# macOS
brew install ffmpeg
```

2. Create and activate virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Unix/macOS
# or
.\env\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## Docker

> ⚠️ **Note:** Docker setup is currently not working in WSL2 environment due to NVIDIA GPU compatibility issues. We recommend using the local setup method above until this is resolved.

To run using Docker (when fixed):

```bash
docker compose up --build
```