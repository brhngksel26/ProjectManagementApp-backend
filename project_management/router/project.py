from fastapi import APIRouter, HTTPException, Depends
from project_management.model.project import Project, ProjectModel
from project_management.utility.function import get_username_id
from project_management.utility.auth_handler import AuthHandler

auth_handler = AuthHandler()
router = APIRouter()

@router.get("/get_project", response_model=list, tags=["Project"])
async def get():
    data_list = Project.objects.all()
    return [data.to_json() for data in data_list]

@router.post("/create_project", tags=["Project"])
async def create(project : ProjectModel, username=Depends(auth_handler.auth_wrapper)):
    project = Project(**project.dict())
    project["admin"] = get_username_id(username)
    project.save()
    return 
