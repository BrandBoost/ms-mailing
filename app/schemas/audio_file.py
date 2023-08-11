from pydantic import BaseModel, Field


class AudioMessageSchema(BaseModel):
    audio_link: str
