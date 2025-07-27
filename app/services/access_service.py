from sqlalchemy.orm import Session
from app.repositories.access_repository import AccessRepository
from app.domain import Access, AccessCreate, AccessUpdate, AccessResponse
from .base_service import BaseService


class AccessService(BaseService[Access, AccessCreate, AccessUpdate, AccessResponse]):
    def __init__(self):
        super().__init__(AccessRepository)
        self.response_schema = AccessResponse
        
        
access_service = AccessService()