from typing import List

from bson import ObjectId
from pydantic import BaseModel, Field

from app.schemas.emails import EmailSchema
from app.schemas.mongo_validators import PyObjectId
from app.schemas.phones import PhonesSchema


class CreateUpdateBases(BaseModel):
    base_name: str
    company_id: str
    project_id: str
    numbers: PhonesSchema
    emails: EmailSchema
    watchers_id: List[str]
    is_hide: bool

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class RetrieveBases(CreateUpdateBases):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
