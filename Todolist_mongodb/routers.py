# routers.py
from fastapi import APIRouter, Depends, HTTPException
from pymongo.database import Database
from bson import ObjectId

from database import get_db
from crud import UserRepository, TodoRepository
from schemas import UserCreate, UserRead, UserLogin, TodoCreate, TodoRead
from datetime import datetime, time
user_router = APIRouter(prefix="/users")
todo_router = APIRouter(prefix="/todos")

@user_router.post("/", response_model=UserRead)
def create_user(user_create: UserCreate, db: Database = Depends(get_db)):
    repo = UserRepository(db)
    try:
        return repo.create({"username": user_create.username, "password": user_create.password})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.get("/", response_model=list[UserRead])
def get_all_users(db: Database = Depends(get_db)):
    repo = UserRepository(db)
    return repo.find_all_users()

@user_router.get("/{user_id}/todos", response_model=list[TodoRead])
def get_all_todos_by_id(user_id: str, db: Database = Depends(get_db)):
    # user_id ist jetzt str(ObjectId)
    repo = TodoRepository(db)
    try:
        ObjectId(user_id)  # Validierung
    except Exception:
        raise HTTPException(status_code=422, detail="Invalid user_id")
    return repo.find_all_todo_by_userid(user_id)

@user_router.post("/authenticate", response_model=UserRead)
def authenticate_user(credentials: UserLogin, db: Database = Depends(get_db)):
    repo = UserRepository(db)
    user = repo.get_user_by_credentails(credentials.username, credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid Username or Password")
    return user

@todo_router.post("/", response_model=TodoRead)
def create_todo(todo: TodoCreate, user_id: str, db: Database = Depends(get_db)):
    repo = TodoRepository(db)
    try:
        uid = ObjectId(user_id)
    except Exception:
        raise HTTPException(status_code=422, detail="Invalid user_id")

    todo_doc = todo.model_dump()
    todo_doc["user_id"] = uid

    if todo_doc.get("deadline") is not None:
        todo_doc["deadline"] = datetime.combine(todo_doc["deadline"], time.min)

    return repo.create(todo_doc)