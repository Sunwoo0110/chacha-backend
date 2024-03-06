from fastapi import APIRouter
from controller.character_controller import CharacterController
from schema.character_schema import CharacterCreateRequest

character_controller = CharacterController()

router = APIRouter(
	prefix="/characters",
    tags=["characters"]
)

@router.post("/create",\
    description="새로운 캐릭터 생성")
async def create_character(character: CharacterCreateRequest):
    new_character = await character_controller.create_character(character.__dict__)
    if new_character:
        return { "result": "success", "character": {"character_id": str(new_character.inserted_id)}}
    else:
        return { "result": "fail" }
    
@router.get("/list",\
    description="캐릭터 리스트 반환) 웹툰/웹소: 1 만화/애니: 2 게임: 3 실존인물: 4 기타: 5")
async def read_characters(category: int):
    character_list = await character_controller.read_characters(category)
    res_list = []
    if character_list == "empty":
        return { "result": "success", "character": res_list}
    
    if character_list:
        for cht in character_list:
            res_list.append({"character_id": str(cht["_id"]), "name": cht["name"], 
                             "description": cht["description"], "img": cht["img"], 
                             "user_cnt": cht["user_cnt"], "chat_cnt": cht["chat_cnt"]})
        return { "result": "success", "character": res_list}
    else:
        return { "result": "fail" }
    
@router.get("/setting",\
    description="캐릭터 설정 확인")
async def read_character(character_id: str):
    cht = await character_controller.read_character(character_id)
    if cht:
        data = {"character_id": str(cht["_id"]), "name": cht["name"], "category": cht["category"], 
                                "description": cht["description"], "setting": cht["setting"], 
                                "example_conv": cht["example_conv"], "open": cht["open"], "img": cht["img"]}
        return { "result": "success", "character": data }
    else:
        return { "result": "fail" }