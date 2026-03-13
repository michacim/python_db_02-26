# database.py
from pymongo import MongoClient
from typing import Generator

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "todo_rest"

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

def get_db() -> Generator:
    # FastAPI Dependency – liefert die DB (pymongo database object)
    yield db