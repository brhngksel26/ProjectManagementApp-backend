from project_management.model.application import Application, ApplicationModel
from fastapi import APIRouter

router = APIRouter()


@router.get("/get_app", response_model = list, tags=["App"])
async def get(id = None):
    if id is None:
        object_value = Application.objects.all()
        return [data.to_json() for data in object_value]

    object_value = Application.objects.filter(id=id)
    return [data.to_json() for data in object_value]


@router.post("/create_app", tags=["App"])
async def create(app : ApplicationModel):
    Application(**app.dict()).save()
    return
