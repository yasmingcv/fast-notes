from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class FileBase(BaseModel):
    url: str
    name: str
    type: str
    note_id: int
    
class FileCreate(FileBase):
    pass

class FileUpdate(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    note_id: Optional[int] = None
    
class FileResponse(FileBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True