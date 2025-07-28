from app.repositories.note_repository import NoteRepository
from app.domain import Note, NoteCreate, NoteUpdate, NoteResponse
from sqlalchemy.orm import Session
from .base_service import BaseService


class NoteService(BaseService[ Note, NoteCreate, NoteUpdate, NoteResponse]):
    def __init__(self):
        super().__init__(NoteRepository)
        self.response_schema = NoteResponse
    
    def get_notes_by_user(self, db: Session, user_id: int, skip: int = 0, limit: int = 100) -> list[NoteResponse]:
        repo = self._get_repository(db)
        notes = repo.get_notes_by_user(user_id, skip, limit)
        return self._to_response_list(notes)
        
        
note_service = NoteService()