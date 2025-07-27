from app.repositories.note_repository import NoteRepository
from app.domain import Note, NoteCreate, NoteUpdate, NoteResponse
from sqlalchemy.orm import Session
from .base_service import BaseService


class NoteService(BaseService[ Note, NoteCreate, NoteUpdate, NoteResponse]):
    def __init__(self):
        super().__init__(NoteRepository)
        self.response_schema = NoteRepository
        
        
note_service = NoteService()