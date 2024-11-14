"""
config.py
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODEL_SIZE: str = "base"
    ALLOWED_AUDIO_FORMATS: list = [".mp3", ".wav", ".m4a", ".ogg"]

    class Config:
        env_file = ".env"


settings = Settings()