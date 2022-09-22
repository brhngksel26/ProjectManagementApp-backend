from fastapi import FastAPI
from mongoengine import connect
from project_management.router import auth, project, card_list
from fastapi.security import HTTPBearer
from fastapi.security import OAuth2PasswordBearer


client = connect("project_management_database", host="mongodb://localhost:27017")

app = FastAPI(
    title = "Project Management App",
    description = "Heybooster Interview Case" 
)

app.include_router(auth.router)
app.include_router(project.router)
app.include_router(card_list.router)


