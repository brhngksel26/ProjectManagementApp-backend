from fastapi import FastAPI
from mongoengine import connect
from project_management.router import applications, auth, project, card_list, triger


client = connect("project_management_database", host="mongodb://localhost:27017")

app = FastAPI(
    title = "Project Management App",
    description = "Heybooster Interview Case" 
)

app.include_router(auth.router)
app.include_router(project.router)
app.include_router(card_list.router)
app.include_router(applications.router)
app.include_router(triger.router)




