# info_db_user
# FFWqoTHYnBP8ZfIT

from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://info_db_user:FFWqoTHYnBP8ZfIT@cluster0.40hnhyp.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi("1"))
client.admin.command("ping")
print("connected")