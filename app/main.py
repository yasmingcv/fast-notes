from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.routers import user_router, auth_router, note_router, file_router

app = FastAPI(title="Fast Notes API", version="1.0.0", description="API for managing notes and users")


@app.get("/")
def hello():
    return {"message": "Hello, World!"}

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(note_router)
app.include_router(file_router)