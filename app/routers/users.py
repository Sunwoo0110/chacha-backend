from fastapi import APIRouter
from controller.user_controller import UserController
from schema.user_schema import UserCreateRequest

user_controller = UserController()

router = APIRouter(
	prefix="/users",
    tags=["users"]
)

@router.post("/register",\
    description="페이지 접속 시 사용자 등록, 기존 회원 시 해당 사용자 반환")
async def create_user(user: UserCreateRequest):
    new_user = await user_controller.create_user(user.uuid)
    if new_user:
        return { "result": "success", "user": {"user_id": str(new_user["_id"]), "chat_cnt": new_user["chat_cnt"]} }
    else:
        return { "result": "fail" }