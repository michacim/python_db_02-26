from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    name:str = Field(min_length=2, max_length=20)
    email:EmailStr


class UserRead(BaseModel):
    id:int
    name:str
    email:EmailStr
    model_config = {"from_attributes": True}


class UserUpdate(BaseModel):
    name:str = Field(min_length=2, max_length=20)
    email:EmailStr

