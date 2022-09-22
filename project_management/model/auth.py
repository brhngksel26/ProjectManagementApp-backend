from mongoengine import Document, StringField
from pydantic import BaseModel


class AuthModel(BaseModel):
    username: str
    password: str


class Auth(Document):
    meta = {"collection": "auths"}
    username: str = StringField(unique=True, required=True)
    password: str = StringField(required=True)
