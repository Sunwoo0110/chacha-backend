from pydantic import BaseModel, Field
from typing import Optional

class CharacterCreateRequest(BaseModel):
    user_id: str = Field(..., example="65daae4171dbf1b50bdf2dbf", 
                    description="사용자 id")
    name: str = Field(..., example="전영중", 
                    description="캐릭터 이름")
    description: str = Field(..., example="가비지타임, 원중고의 농구 선수", 
                    description="캐릭터 한 줄 소개")
    category: int  = Field(..., example=1, 
                    description="캐릭터 카테고리) 웹툰/웹소: 1 만화/애니: 2 게임: 3 실존인물: 4 기타: 5")
    setting: Optional[str] = Field(..., example="고등학생 / 원중고등학교의 농구선수 / 스몰포워드 / 성준수랑 친구임 / 팀원들을 잘 챙김", 
                    description="캐릭터 설정")
    example_conv: Optional[str] = Field(..., example="요~ 준수 / 십일 분의 일, 일일일. 간첩신고해도 되겠어. / 누가 계속 농구하래!", 
                    description="캐릭터 말투")
    personality: Optional[str] = Field(..., example="차분함 / 기가 셈 / 친절함 / 멘헤라임", 
                    description="캐릭터 성격")
    open: bool = Field(..., 
                    description="캐릭터 공개 여부")
    img: Optional[str] = Field(...,
                    description="캐릭터 사진(S3 버킷 url)")
    user_cnt: int = Field(..., example=0,
                    description="캐릭터 사용자 수")

    # class Config:
    #     arbitrary_types_allowed = True
    #     json_encoders = {ObjectId: str}