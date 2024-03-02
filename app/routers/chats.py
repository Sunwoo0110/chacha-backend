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
    name, img, response, chat_cnt = await chat_controller.create_chat(chat)
    
    if response:
        return { "result": "success", "chat": {"name": name, "img": img, "response": response, "chat_cnt": chat_cnt}}
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
    
@router.get("/history", \
    description="기존 채팅 답변 불러오기")
async def read_chats(user_id: str, character_id: str):
    chat_list = await chat_controller.read_chats(user_id, character_id)
    if chat_list == "empty":
        return { "result": "success", "chats": []}
    
    if chat_list:
        # for chat in chat_list:
        #     res_list.append({"name": chat["name"], "img": chat["img"], 
        #                      "user_chat": chat["user_chat"], "ai_chat": chat["ai_chat"]})
        return { "result": "success", "chats": chat_list}
    else:
        return { "result": "fail" }
        