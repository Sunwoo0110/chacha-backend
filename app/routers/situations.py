from fastapi import APIRouter
from controller.situation_controller import SituationController
from schema.situation_schema import SituationCreateRequest

situation_controller = SituationController()

router = APIRouter(
	prefix="/situations",
    tags=["situations"]
)

@router.post("/create",\
    description="새로운 상황 생성")
async def create_situation(situation: SituationCreateRequest):
    new_situation = await situation_controller.create_situation(situation.__dict__)
    if new_situation:
        return { "result": "success", "situation": {"situation_id": str(new_situation.inserted_id)}}
    else:
        return { "result": "fail" }