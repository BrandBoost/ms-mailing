from typing import List
import re
from pydantic import BaseModel, Field, validator
from fastapi import HTTPException


class EmailSchema(BaseModel):
    emails: List[str] = Field(description="List of mail addresses for mailing with Gmail", unique_items=True)
    text: str = Field(description="Text for mailing with Gmail")

    @validator('emails')
    def validate_email_addresses(cls, values):
        for value in values:
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
                raise HTTPException(detail=f'Invalid email address: {value}', status_code=403)

        return values
