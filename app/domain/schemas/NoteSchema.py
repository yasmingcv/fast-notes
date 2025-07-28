from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# Schema base para Nota
class NoteBase(BaseModel):
    title: str
    content: str
    user_id: Optional[int] = None
class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class NoteResponse(NoteBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
