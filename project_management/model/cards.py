
from enum import Enum
from pydantic import BaseModel
from project_management.model.project import Project
from datetime import datetime
from mongoengine import (
    DateTimeField,
    Document,
    EmbeddedDocument,
    EmbeddedDocumentListField,
    ReferenceField,
    StringField,
    BooleanField,
    EnumField,
    ListField
)
from project_management.model.account import Account, AccountModel

class CardStatus(Enum):
    PROGRESS = "in progress"
    STARTED = "started"
    CONTROL = "in control"
    COMPLETED = "completed"

class CommentModel(BaseModel):
    comment : str
    created_time : datetime

class CardModel(BaseModel):
    description : str
    members : str
    status : CardStatus
    comment : list[CommentModel]
    created_time : datetime
    started_time : datetime
    finish_time : datetime
    is_completed : bool

class Comment(EmbeddedDocument):
    comment = StringField()
    account = ReferenceField(Account)
    created_time = DateTimeField(default=datetime.now)

class Card(Document):
    meta = {"collection": "cards"}
    description = StringField()
    status = EnumField(CardStatus)
    comment = EmbeddedDocumentListField(Comment)
    members = ListField(ReferenceField(Account, unique=True))
    created_time = DateTimeField(default=datetime.now)
    started_time = DateTimeField(required=True)
    finish_time = DateTimeField(required=True)
    is_completed = BooleanField(default=False)