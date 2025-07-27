from sqlalchemy.orm import Session
from typing import Optional
from app.domain import User, UserCreate, UserUpdate
from .base_repository import BaseRepository


class UserRepository(BaseRepository[User, UserCreate]):
    def __init__(self, db: Session):
        super().__init__(db, User)
    
    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()
    
    def get_by_name(self, name: str) -> Optional[User]:
        return self.db.query(User).filter(User.name == name).first()

    def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        return self.update(user_id, user_update)