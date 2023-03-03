import uuid

from pydantic import BaseModel


class User(BaseModel):
    id: uuid.UUID
    username: str
    password: str


class UserIn(BaseModel):
    username: str
    password: str


class Plant(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    description: str
