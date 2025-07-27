from sqlalchemy.orm import Session
from app.repositories.access_repository import AccessRepository
from app.domain import Access, AccessCreate, AccessUpdate, AccessResponse
from .base_service import BaseService


class AccessService(BaseService[Access, AccessCreate, AccessUpdate, AccessResponse]):
    def __init__(self):
        super().__init__(AccessRepository)
        self.response_schema = AccessResponse
        
    def get_active_access_token(self, db: Session, token: str):
        repo = self._get_repository(db)
        return repo.get_active_access_token(token)

        
        
access_service = AccessService()