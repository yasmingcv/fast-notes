from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


# Schema base para User
class UserBase(BaseModel):
    email: EmailStr
    name: str


# Schema para criação de usuário (recebe senha)
class UserCreate(UserBase):
    password: str


# Schema para atualização de usuário (campos opcionais)
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    password: Optional[str] = None


# Schema para resposta (sem senha)
class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
    