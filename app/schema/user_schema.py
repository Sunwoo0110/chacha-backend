from pydantic import BaseModel, Field

class UserCreateRequest(BaseModel):
    uuid: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", 
                    description="사용자 uuid")

