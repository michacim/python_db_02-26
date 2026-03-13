# schemas.py
from pydantic import BaseModel, Field
from datetime import date
from enum import Enum

class TodoState(str, Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class TodoBase(BaseModel):
    task: str = Field(..., min_length=2, max_length=100)
    description: str | None = None
    deadline: date | None = None
    state: TodoState = TodoState.OPEN

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id: str
    user_id: str

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str = Field(min_length=5, max_length=100)

class UserRead(UserBase):
    id: str
    todos: list[TodoRead] = []

class UserLogin(BaseModel):
    username: str
    password: str