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
    description="캐릭터 리스트 반환")
async def read_characters():
    character_list = await character_controller.read_characters()
    res_list = []
    if character_list:
        for cht in character_list:
            res_list.append({"character_id": str(cht["_id"]), "name": cht["name"], 
                             "setting": cht["setting"], "img": cht["img"], 
                             "accent": cht["accent"], "personality": cht["personality"], "user_cnt": cht["user_cnt"]})
        return { "result": "success", "character": res_list}
    else:
        return { "result": "fail" }