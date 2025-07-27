from sqlalchemy.orm import Session
from app.domain import Access, AccessCreate
from .base_repository import BaseRepository


class AccessRepository(BaseRepository[Access, AccessCreate]):
    def __init__(self, db: Session):
        super().__init__(db, Access)
        
    def get_active_access_token(self, token:str):
        return self.db.query(Access).filter(Access.token == token and Access.token).first()