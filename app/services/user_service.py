from app.repositories import user_repository
from app.domain import UserCreate, UserUpdate, UserResponse
from sqlalchemy.orm import Session
from app.utils import hash_password, verify_password

def create_user(db: Session, user_create: UserCreate):
    existing_user = user_repository.get_user_by_email(db, user_create.email)
    if existing_user:
        raise ValueError("User with this email already exists")
    user_create.password = hash_password(user_create.password)
    return user_repository.create_user(db, user_create)

def get_user_by_email(db: Session, email: str):
    user = user_repository.get_user_by_email(db, email)
    if not user:
        raise ValueError("User not found")
    # Valida a lista de usuários e converte para o formato de resposta do pydantic
    return UserResponse.model_validate(user, from_attributes=True)

def update_user(db: Session, user_id: int, user_update: UserUpdate):
    user = user_repository.update_user(db, user_id, user_update)
    if not user:
        raise ValueError("User not found")
    # Valida a lista de usuários e converte para o formato de resposta do pydantic
    return UserResponse.model_validate(user, from_attributes=True)

def list_users(db: Session, skip: int = 0, limit: int = 10):
    users = user_repository.list_users(db, skip, limit)
    # Valida a lista de usuários e converte para o formato de resposta do pydantic
    return [UserResponse.model_validate(user, from_attributes=True) for user in users]
