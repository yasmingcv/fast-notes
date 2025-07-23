from app.database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class File(Base):
    __tablename__ = "files"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(), nullable=False)
    name = Column(String(), nullable=False)
    type = Column(String(), nullable=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Chave estrangeira 
    note_id = Column(Integer, ForeignKey("notes.id"), nullable=False)
    
    # Relacionamento
    note = relationship("Note", back_populates="files")