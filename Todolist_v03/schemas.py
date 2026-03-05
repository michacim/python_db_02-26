## Schema für Todo und User
from pydantic import BaseModel , Field
from datetime import date
from enum import Enum

# ------------------- User --------------------------


class UserBase(BaseModel):
    username:str

class UserCreate(UserBase):
    password: str= Field(min_length=5, max_length=100)

class UserRead(UserBase):
    id:int
    todos:list[TodoRead] = []


class UserLogin(BaseModel):
    username:str
    password:str

#------------- Todo ----------------------
class TodoState(Enum):
    OPEN="OPEN"
    IN_PROGRESS="IN_PROGRESS"
    DONE="DONE"

class TodoBase(BaseModel):
    task:str = Field(...,min_length=2,max_length=100)# ... Pflichtfeld
    description:str | None = None
    deadline:date | None = None
    state:str = TodoState.OPEN  #FIXME TodoState
class TodoCreate(TodoBase):
    pass
class TodoRead(TodoBase):
    id:int
    user_id:int