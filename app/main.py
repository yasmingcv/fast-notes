from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db

app = FastAPI(title="Fast Notes API", version="1.0.0")


@app.get("/")
def hello():
    return {"message": "Hello, World!"}