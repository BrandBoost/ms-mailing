from typing import List

from pydantic import BaseModel, Field


class WhatsappSchema(BaseModel):
    phones: List[str] = Field(description="List of phones for mailing with WhatsApp", unique_items=True)
    text: str = Field(description="Text for mailing with WhatsApp")
