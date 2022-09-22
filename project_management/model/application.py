from pydantic import BaseModel
from mongoengine import Document, StringField


class ApplicationModel(BaseModel):
    name : str
    token : str

class Application(Document):
    meta = {"collection": "applications"}
    name = StringField(required=True)
    token = StringField(required=True)
