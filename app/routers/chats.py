from fastapi import APIRouter
from controller.chat_controller import ChatController
from schema.chat_schema import ChatCreateRequest

chat_controller = ChatController()

router = APIRouter(
	prefix="/chats",
    tags=["chats"]
)

@router.post("/response",\
    description="채팅 답변 생성")
async def create_chat(chat: ChatCreateRequest):
    name, img, response = await chat_controller.create_chat(chat)
    
    if response:
        return { "result": "success", "chat": {"name": name, "img": img, "response": response}}
    else:
        return { "result": "fail" }
    
@router.get("/cntupdate",\
    description="캐릭터의 채팅 횟수 증가(채팅방 들어갈 시 처음 한번만 호출)")
async def update_chat_cnt(character_id: str):    
    result = await chat_controller.update_chat_cnt(character_id)
    if result:
        return { "result": "success", "user_cnt": result }
    else:
        return { "result": "fail" }