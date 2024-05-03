from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo

class ChatCreateRequest(BaseModel):
    user_id: str = Field(..., example="65daae4171dbf1b50bdf2dbf", 
                    description="사용자 id")
    character_id: str = Field(..., example="65dac988d53681899908cc23", 
                    description="캐릭터 id")
    user_chat: str = Field(..., example="안녕하세요",
                    description="사용자 채팅")
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(ZoneInfo("Asia/Seoul")))