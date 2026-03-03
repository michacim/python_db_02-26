from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from models import User
from database import Base, engine, get_db
from schema import UserCreate, UserRead, UserUpdate
from crud import UserRepository




user_router = APIRouter()

@user_router.post("/users/", response_model=UserRead)
def create_user(user:UserCreate, db:Session=Depends(get_db)):
    repo = UserRepository(db)

    if repo.get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already registered!")

    # UserCreate zu "normalen" User konvertieren
    # macht aus einem Pydantic-Model ein normales Python-dict
    new_user = User(**user.model_dump())
    return repo.create_user(new_user)
