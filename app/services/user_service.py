from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.domain import User, UserCreate, UserUpdate, UserResponse
from app.utils import hash_password, verify_password
from .base_service import BaseService


class UserService(BaseService[User, UserCreate, UserUpdate, UserResponse]):
    def __init__(self):
        super().__init__(UserRepository)
        self.response_schema = UserResponse

    def create(self, db: Session, user: UserCreate) -> UserResponse:
        repo = self._get_repository(db)
        
        if repo.get_by_email(user.email) is not None:
            raise ValueError("User with this email already exists")
        
        # Hash the password before saving
        hashed_obj = user.model_copy()
        hashed_obj.password = hash_password(user.password)
        
        user = repo.create(hashed_obj)
        return self._to_response_schema(user)
    
    def get_user_by_email(self, db: Session, email: str) -> UserResponse:
        repo = self._get_repository(db)
        user = repo.get_by_email(email)
        if not user:
            return None
        return self._to_response_schema(user)

    def get_user_by_name(self, db: Session, name: str) -> UserResponse:
        repo = self._get_repository(db)
        user = repo.get_by_name(name)
        if not user:
            return None
        return self._to_response_schema(user)
    
    def update(self, db: Session, id: int, user_update: UserUpdate) -> UserResponse:
        repo = self._get_repository(db)
        user = repo.get(id)
        print('user por id', user)
        if not user:
            return None
        
        if user.email != user_update.email:
            user_by_email = repo.get_by_email(user_update.email)
            print('user por email', user_by_email)
            if (user_by_email is not None and user_by_email.id != id):
                raise ValueError("User with this email already exists")
            
        return repo.update(id, user_update)


# Instância global do service
user_service = UserService()