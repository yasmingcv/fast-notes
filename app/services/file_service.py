from app.repositories.file_repository import FileRepository
from app.domain import File, FileCreate, FileUpdate, FileResponse
from sqlalchemy.orm import Session
from .base_service import BaseService


class FileService(BaseService[File, FileCreate, FileUpdate, FileResponse]):
    def __init__(self):
        super().__init__(FileRepository)
        self.response_schema = FileResponse
        
file_service = FileService()