from typing import Optional, List
from pydantic import BaseModel, Field, HttpUrl
from bson import ObjectId
from datetime import datetime

def PyObjectId(v: str):
    return ObjectId(v)

class Characters(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    user_id: str  # MongoDB의 ObjectId를 문자열로 저장
    name: str ## 캐릭터명
    description: str ## 한줄소개
    category: int = 0 ## 카테고리
    setting: Optional[str] = None
    example_conv: Optional[str] = None
    personality: Optional[str] = None
    open: bool
    img: Optional[str] = None
    user_cnt: int = 0
    chat_cnt: int = 0
    created_at: Optional[datetime]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}