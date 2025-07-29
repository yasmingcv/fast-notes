from sqlalchemy.orm import Session
from typing import Optional, List
from app.domain import File, FileCreate, FileUpdate
from app.domain.schemas import NoteResponse
from .base_repository import BaseRepository

class FileRepository(BaseRepository[File, FileCreate]):
    def __init__(self, db: Session):
        super().__init__(db, File)