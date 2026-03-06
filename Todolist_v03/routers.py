from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User, Todo
from crud import UserRepository, TodoRepository
from schemas import *


user_router= APIRouter(prefix="/users")
todo_router=APIRouter(prefix="/todos")

@user_router.post("/",response_model=UserRead)
def create_user(user_create:UserCreate, db:Session =Depends(get_db)):
    repo = UserRepository(db)
    new_user =User(username = user_create.username, 
                   password = user_create.password)
    return repo.create(new_user)


@user_router.get("/", response_model=list[UserRead] )
def get_all_users(db:Session=Depends(get_db)):
    repo = UserRepository(db)
    return repo.find_all_users()

@user_router.get("/{user_id}/todos",response_model=list[TodoRead])# http://localhost:8000/users/2/todos
def get_all_todos_by_id(user_id:int, db:Session=Depends(get_db)):
    repo = TodoRepository(db)
    return repo.find_all_todo_by_userid(user_id)


@user_router.post("/authenticate",response_model=UserRead)# http://localhost:8000/users/authenticate
def authenticate_user(credentails:UserLogin,db:Session=Depends(get_db)):
    repo =  UserRepository(db)
    user = repo.get_user_by_credentails(credentails.username,credentails.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid Username or Password")
    return user

#----------------Todo----------------------------

@todo_router.post("/",response_model=TodoRead)#  
def create_todo(todo:TodoCreate, user_id:int, db:Session=Depends(get_db)):
    repo = TodoRepository(db)
    todo_db = Todo( **todo.model_dump(),user_id=user_id )
    return repo.create(todo_db)