from pydantic import BaseModel, Field
from typing import Optional

class SituationCreateRequest(BaseModel):
    user_id: str = Field(..., example="65daae4171dbf1b50bdf2dbf", 
                    description="사용자 id")
    character_id: str = Field(..., example="65dac988d53681899908cc23", 
                    description="캐릭터 id")
    name: str = Field(..., example="엘사", 
                    description="캐릭터 이름")
    description: str = Field(..., example="엘사랑 결혼하기", 
                    description="대화 상황")
    first_conv: Optional[str] = Field(..., example="사랑해", 
                    description="첫 대화")