from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
import pymongo


#uvicorn main:app --reload
app = FastAPI()



app.route('api/v1/messages/',methods=['GET'])
def get_messages():
    pass











