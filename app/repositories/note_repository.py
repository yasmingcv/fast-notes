from sqlalchemy.orm import Session, joinedload
from typing import Optional, List
from app.domain import Note, NoteCreate, NoteUpdate
from app.domain.schemas import NoteResponse
from .base_repository import BaseRepository

class NoteRepository(BaseRepository[Note, NoteCreate]):
    def __init__(self, db: Session):
        super().__init__(db, Note)
    
    def get_notes_by_user(self, user_id: int, skip: int = 0, limit: int = 100) -> List[Note]:
        return self.db.query(Note).options(joinedload(Note.files)).filter(Note.user_id == user_id).offset(skip).limit(limit).all()
