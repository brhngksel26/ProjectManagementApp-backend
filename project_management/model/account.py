from tokenize import String
from mongoengine import Document, StringField, ReferenceField
from pydantic import BaseModel
from project_management.model.auth import Auth


class AccountModel(BaseModel):
    name : str
    surname : str
    role : str

class Account(Document):
    name = StringField(unique=True, required=True)
    surname = StringField(unique=True, required=True)
    role = StringField()
    auth_id = ReferenceField(Auth, unique=True, required=True)