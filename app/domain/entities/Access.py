from app.database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Access(Base):
    __tablename__ = "accesses"
    
    id = Column(Integer, primary_key=True, index=True)
    token = Column(Text, nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Chave estrangeira
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relacionamento
    user = relationship("User", back_populates="accesses")