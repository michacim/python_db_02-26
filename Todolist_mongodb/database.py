# database.py
from pymongo import MongoClient
from typing import Generator

#MONGO_URL = "mongodb://localhost:27017"
MONGO_URL = "mongodb+srv://info_db_user:FFWqoTHYnBP8ZfIT@cluster0.40hnhyp.mongodb.net/?appName=Cluster0"
DB_NAME = "todo_rest"

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

def get_db() -> Generator:
    # FastAPI Dependency – liefert die DB (pymongo database object)
    yield db