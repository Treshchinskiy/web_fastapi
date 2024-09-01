from pymongo import MongoClient

"""
client = MongoClient("localhost", 27017)

db = client.neuraldb

people = db.people 

people.insert_one({"name":"Mike","Age":32})

"""
from pydantic import BaseModel

class Message(BaseModel):
    content: str



