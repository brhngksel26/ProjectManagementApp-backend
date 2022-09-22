from pydantic import BaseModel
from project_management.model.project import Project, ProjectModel
from datetime import datetime
from mongoengine import (
    Document,
    ReferenceField,
    StringField,
    ListField
)
from project_management.model.cards import CardModel, Card


class CardListInput(BaseModel):
    title : str

class CardListOutput(BaseModel):
    title : str 
    cards : list[CardModel]
    projects : ProjectModel = None


class CardList(Document):
    meta = {"collection": "card_lists"}
    title = StringField(required=True)
    cards = ListField(ReferenceField(Card))
    project = ReferenceField(Project, required=True)

