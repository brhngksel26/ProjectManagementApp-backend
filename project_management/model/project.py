from datetime import  datetime
from pydantic import BaseModel
from project_management.model.account import Account, AccountModel
from enum import Enum

from mongoengine import (
    DateTimeField,
    Document,
    ReferenceField,
    StringField,
    ListField,
    EnumField
)


class ProjectModel(BaseModel):
    name : str
    description : str
    status : str
    members : list[AccountModel] = None


class ProjectStatus(Enum):
    ACTIVATE = 'activate'
    ARCHIVED = 'archived'
    DONE = 'done'


class Project(Document):
    meta = {"collection": "projects"}
    name = StringField(required=True)
    description = StringField()
    status = EnumField(ProjectStatus, default=ProjectStatus.ACTIVATE)
    created_time = DateTimeField(default=datetime.now)
    admin = ReferenceField(Account)
    members = ListField(ReferenceField(Account))
