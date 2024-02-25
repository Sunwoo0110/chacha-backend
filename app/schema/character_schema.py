from pydantic import BaseModel, Field
from typing import Optional

class CharacterCreateRequest(BaseModel):
    user_id: str = Field(..., example="65daae4171dbf1b50bdf2dbf", 
                    description="사용자 id")
    name: str = Field(..., example="엘사", 
                    description="캐릭터 이름")
    setting: Optional[str] = Field(..., example="디즈니 애니메이션 겨울왕국 주인공/ 얼음 마법사 / 안나의 친언니", 
                    description="캐릭터 설정")
    accent: Optional[str] = Field(..., example="난 어차피 추위를 안 타. / 방금 만난 남자와 결혼해서는 안 돼! / 두려움은 불신에서 나오는 거야. / 내가 할 일은 마법에 걸린 숲으로 가서 그 목소리를 찾아가는 거야. / 다 잊어! 다 잊어! 더 이상 참지 않아! / 어차피 추위는 날 힘들게 하지 못해. / 두려움은 믿지 못할 것이야. / 나의 힘이 커지는 것을 느낄 때마다 매일이 조금씩 더 힘들어져. 내 속의 일부가 알지 못하는 곳으로 가기를 원한다는 사실을 모르겠니?", 
                    description="캐릭터 말투")
    personality: Optional[str] = Field(..., example="까칠/ 두려움/ 용기/ 냉정/ 믿음/ 강인함", 
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