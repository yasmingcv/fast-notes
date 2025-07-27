from sqlalchemy.orm import Session
from typing import Optional
from app.domain import Note, NoteCreate, NoteUpdate
from app.domain.schemas import NoteResponse
from .base_repository import BaseRepository

class NoteRepository(BaseRepository[Note, NoteCreate]):
    def __init__(self, db: Session):
        super().__init__(db, Note)
