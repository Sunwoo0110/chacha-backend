from typing import Optional, List
from pydantic import BaseModel, Field, HttpUrl
from bson import ObjectId

def PyObjectId(v: str):
    return ObjectId(v)

class Situations(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    user_id: str
    character_id: str
    description: str
    first_conv: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}