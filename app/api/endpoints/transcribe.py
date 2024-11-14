"""
transcribe.py
"""

from fastapi import APIRouter, UploadFile, File
from app.services.whisper_service import WhisperService
from app.schemas.transcription import TranscriptionResponse

router = APIRouter(prefix="/api/v1")


@router.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(file: UploadFile = File(...)):
    whisper_service = WhisperService()
    result = await whisper_service.transcribe(file)
    return result