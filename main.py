from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

class User(BaseModel):
    FIO: str
    email: str
    phoneNumber: str
    role: str

@app.post("/user/")
async def create_item(user: User):
    return user
