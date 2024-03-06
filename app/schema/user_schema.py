from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from zoneinfo import ZoneInfo

class UserCreateRequest(BaseModel):
    uuid: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", 
                    description="사용자 uuid")
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(ZoneInfo("Asia/Seoul")))

