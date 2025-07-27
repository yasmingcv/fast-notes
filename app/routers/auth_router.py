from fastapi import APIRouter, Depends, HTTPException, status
from app.auth import auth_service
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/login")
def authenticate(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth_service.login(form_data.username, form_data.password, db)
    
    
