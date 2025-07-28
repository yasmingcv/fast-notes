from sqlalchemy.orm import Session
from typing import Optional, List
from app.domain import Note, NoteCreate, NoteUpdate
from app.domain.schemas import NoteResponse
from .base_repository import BaseRepository

class NoteRepository(BaseRepository[Note, NoteCreate]):
    def __init__(self, db: Session):
        super().__init__(db, Note)
    
    def get_notes_by_user(self, user_id: int, skip: int = 0, limit: int = 100) -> List[Note]:
        """Busca todas as notas de um usuário específico"""
        return self.db.query(Note).filter(Note.user_id == user_id).offset(skip).limit(limit).all()
