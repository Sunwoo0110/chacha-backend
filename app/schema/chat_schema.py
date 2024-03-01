from pydantic import BaseModel, Field
from typing import Optional

class ChatCreateRequest(BaseModel):
    user_id: str = Field(..., example="65daae4171dbf1b50bdf2dbf", 
                    description="사용자 id")
    character_id: str = Field(..., example="65dac988d53681899908cc23", 
                    description="캐릭터 id")
    # situation_id: str = Field(..., example="65dabc6d6af9f66286b55ddd", 
    #                 description="상황 id")
    # name: str = Field(..., example="엘사", 
    #                 description="캐릭터 이름")
    # setting: Optional[str] = Field(..., example="디즈니 애니메이션 겨울왕국 주인공/ 얼음 마법사 / 안나의 친언니", 
                    # description="캐릭터 설정")
    user_chat: str = Field(..., example="안녕하세요",
                    description="사용자 채팅")

    # class Config:
    #     arbitrary_types_allowed = True
    #     json_encoders = {ObjectId: str}