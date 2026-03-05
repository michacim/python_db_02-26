from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from models import User
from database import Base, engine, get_db
from schema import UserCreate, UserRead, UserUpdate
from crud import UserRepository




user_router = APIRouter()

@user_router.post("/users/", response_model=UserRead)
def create_user(user_create:UserCreate, db:Session=Depends(get_db)):
    repo = UserRepository(db)

    if repo.get_user_by_email(user_create.email):
        raise HTTPException(status_code=400, detail="Email already registered!")

    # UserCreate zu "normalen" User konvertieren
    # macht aus einem Pydantic-Model ein normales Python-dict
    new_user = User(**user_create.model_dump())
    return repo.create_user(new_user)
@user_router.get("/users/",response_model=list[UserRead])
def get_all_users(db:Session=Depends(get_db)):
    repo = UserRepository(db)
    return repo.get_all_users()



@user_router.put("/users/{user_id}",response_model=UserRead)
def update_user(user_id:int, user_update:UserUpdate, db:Session = Depends(get_db)):
    repo = UserRepository(db)


    #user_obj =User(id=user_id, **user_update.model_dump() ) # >>> Kurzform
    user_obj =User(id=user_id, name=user_update.name, emmail=user_update.email )#User(id=user_id, name="Max" ,email="max@web.de")

    user = repo.update_user(user_obj)

    return user

######## Aufgabe ##################

#1)
# @user_router.get("/users/", response_model=-list[UserRead])
# def get_all_users(db:Session=Depends(get_db)):
#     pass

#2)Zusatz

# update für crud.py
# definiere update per put
# def update_user(user_id:int, user_update:UserUpdate)


