import uuid

from pydantic import BaseModel


class UserIn(BaseModel):
    username: str
    password: str


class User(UserIn):
    id: uuid.UUID


class Plant(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    description: str
