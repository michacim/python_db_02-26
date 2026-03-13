# crud.py
from pymongo.database import Database
from bson import ObjectId
from datetime import date
from util import hash_password, verify_password

ALLOWED_STATES = {"OPEN", "IN_PROGRESS", "DONE"}

def _oid(id_str: str) -> ObjectId:
    return ObjectId(id_str)

def _todo_to_read(doc: dict) -> dict:
    return {
        "id": str(doc["_id"]),
        "task": doc.get("task"),
        "description": doc.get("description"),
        "deadline": doc.get("deadline"),
        "state": doc.get("state"),
        "user_id": str(doc.get("user_id")),
    }

def _user_to_read(doc: dict) -> dict:
    return {
        "id": str(doc["_id"]),
        "username": doc.get("username"),
        "todos": [],
    }

class TodoRepository:
    def __init__(self, db: Database):
        self.todos = db["todos"]

    def create(self, todo_doc: dict) -> dict:
        res = self.todos.insert_one(todo_doc)
        created = self.todos.find_one({"_id": res.inserted_id})
        return _todo_to_read(created)

    def find_all_todo_by_userid(self, user_id: str) -> list[dict]:
        cur = self.todos.find({"user_id": _oid(user_id)}).sort([("deadline", 1), ("_id", 1)])
        return [_todo_to_read(d) for d in cur]

    def find_open_todos(self, user_id: str) -> list[dict]:
        cur = self.todos.find({"user_id": _oid(user_id), "state": "OPEN"})
        return [_todo_to_read(d) for d in cur]

    def find_todos_by_task(self, user_id: str, task: str) -> list[dict]:
        # case-insensitive contains -> regex
        cur = self.todos.find({
            "user_id": _oid(user_id),
            "task": {"$regex": task, "$options": "i"}
        })
        return [_todo_to_read(d) for d in cur]

    def update_todo_state(self, todo_id: str, new_state: str) -> dict | None:
        if new_state not in ALLOWED_STATES:
            raise ValueError("Invalid state")

        res = self.todos.update_one({"_id": _oid(todo_id)}, {"$set": {"state": new_state}})
        if res.matched_count == 0:
            return None
        doc = self.todos.find_one({"_id": _oid(todo_id)})
        return _todo_to_read(doc)


class UserRepository:
    def __init__(self, db: Database):
        self.users = db["users"]

    def create(self, user_doc: dict) -> dict:
        if user_doc is None:
            raise ValueError("user darf nicht None sein")
        if not user_doc.get("username"):
            raise ValueError("username ist Pflicht")
        if not user_doc.get("password"):
            raise ValueError("password ist Pflicht")

        existing = self.users.find_one({"username": user_doc["username"]})
        if existing:
            raise ValueError("username existiert bereits")

        user_doc["password"] = hash_password(user_doc["password"])
        res = self.users.insert_one(user_doc)
        created = self.users.find_one({"_id": res.inserted_id})
        return _user_to_read(created)

    def get_user_by_credentails(self, username: str, password: str) -> dict | None:
        if not username or not password:
            return None
        user = self.users.find_one({"username": username})
        if not user:
            return None
        return _user_to_read(user) if verify_password(password, user.get("password", "")) else None

    def find_all_users(self) -> list[dict]:
        return [_user_to_read(u) for u in self.users.find({}).sort([("_id", 1)])]