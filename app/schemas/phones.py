import re
from typing import List

from fastapi import HTTPException
from pydantic import BaseModel, Field, validator


class PhonesSchema(BaseModel):
    phones: List[str] = Field(description="List of phones for mailing with phones", unique_items=True)
    text: str = Field(description="Text for mailing with phones")

    @validator('phones')
    def validate_phone_numbers(cls, values):
        patterns = [
            r"^\+code\(\d{3}\)\d{3}-\d{2}-\d{2}$",
            r"^code\d{11}$",
            r"^\+\d{1,4}\d{11}$",
            r"^code\(\d{3}\)\d{3}-\d{2}-\d{2}$"
        ]
        valid_formats = [pattern.replace("code", r"\d{1,4}") for pattern in patterns]

        for value in values:
            if not any(re.match(pattern, value) for pattern in valid_formats):
                raise HTTPException(detail=f'Invalid phone number format: {value}', status_code=422)

        return values
