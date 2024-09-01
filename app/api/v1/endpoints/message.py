from fastapi import APIRouter, Form
from .. import models
from app.models.message import Message
from app.core.database import db 


router = APIRouter()

messages_collection = db["messages"]

@router.get("/messages/")
async def get_messages():
    messages = list(messages_collection.find({}))
    return messages

@router.post("/message/")
async def post_message(content: str = Form(...)):
    message = Message(content=content)
    result = messages_collection.insert_one(message.dict())
    return {"id": str(result.inserted_id), "message": content}
