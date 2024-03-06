from typing import Optional, List
from pydantic import BaseModel, Field, HttpUrl
from bson import ObjectId
from datetime import datetime

def PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)

class Users(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    uuid: str
    chat_cnt: int = 0
    created_at: Optional[datetime]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}