"""
transcription.py
"""

from pydantic import BaseModel
from typing import List

class Segment(BaseModel):
    start: float
    end: float
    text: str

class TranscriptionResponse(BaseModel):
    text: str
    segments: List[Segment]