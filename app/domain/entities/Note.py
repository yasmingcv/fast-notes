from app.database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Note(Base):
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Chave estrangeira
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relacionamento
    # back_populates -> cria uma relação bidirecional
    user = relationship("User", back_populates="notes")
    files = relationship("File", back_populates="note", cascade="all, delete-orphan")
    