from typing import Optional, List
from pydantic import BaseModel, Field, HttpUrl
from bson import ObjectId

def PyObjectId(v: str):
    return ObjectId(v)

class Characters(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    user_id: str  # MongoDB의 ObjectId를 문자열로 저장
    name: str
    setting: Optional[str] = None
    accent: Optional[str] = None
    personality: Optional[str] = None
    open: bool
    img: Optional[str] = None
    user_cnt: int = 0

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}