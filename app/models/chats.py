from typing import Optional, List
from pydantic import BaseModel, Field, HttpUrl
from bson import ObjectId
from datetime import datetime

def PyObjectId(v: str):
    return ObjectId(v)

class Chats(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    user_id: str
    character_id: str
    # situation_id: str
    user_chat: str
    ai_chat: str
    created_at: Optional[datetime]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}