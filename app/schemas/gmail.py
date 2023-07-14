from typing import List

from pydantic import BaseModel, Field


class GmailSchema(BaseModel):
    emails: List[str] = Field(description="List of mail addresses for mailing with Gmail", unique_items=True)
    text: str = Field(description="Text for mailing with Gmail")
