from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class AccessBase(BaseModel):
    token: str
    active: bool = True
    user_id: int
    
class AccessCreate(AccessBase):
    pass

class AccessUpdate(BaseModel):
    token: Optional[str] = None
    active: Optional[bool] = None
    user_id: Optional[int] = None
    
class AccessResponse(AccessBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True