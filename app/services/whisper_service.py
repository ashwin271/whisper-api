"""
whisper_service.py
"""

import whisper
from pathlib import Path
import tempfile


class WhisperService:
    def __init__(self):
        self.model = whisper.load_model("base")  
        # model base or "tiny", "small", "medium", "large"

    async def transcribe(self, file):
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(file.filename).suffix) as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_file.flush()

            # Perform transcription
            result = self.model.transcribe(temp_file.name)

        # Clean up
        Path(temp_file.name).unlink()

        return {
            "text": result["text"],
            "segments": result["segments"]
        }