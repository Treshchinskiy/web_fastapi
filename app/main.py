from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from .models.message import Message

app = FastAPI()

# Подключение к базе данных MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["message_db"]
messages_collection = db["messages"]

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/view-messages", response_class=HTMLResponse)
async def view_messages(request: Request):
    messages = list(messages_collection.find({}))
    return templates.TemplateResponse("view_messages.html", {"request": request, "messages": messages})

@app.get("/add-message", response_class=HTMLResponse)
async def add_message_page(request: Request):
    return templates.TemplateResponse("add_message.html", {"request": request})

@app.post("/api/v1/message/")
async def post_message(content: str = Form(...)):
    message = Message(content=content)
    result = messages_collection.insert_one(message.dict())
    return {"id": str(result.inserted_id), "message": content}
