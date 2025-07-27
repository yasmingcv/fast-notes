from sqlalchemy.orm import Session
from app.services import user_service, access_service
from app.utils import bcrypt, jwt
from app.domain import AccessCreate
from fastapi import HTTPException, status, Depends
from datetime import timedelta
from app.database import get_db
from app.domain.entities.User import User
from app.domain.entities.Access import Access
from app.services import access_service, user_service
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def login(email: str, password: str, db: Session):
    user = user_service.get_user_by_email(db, email)
    print(user)
    print(bcrypt.verify_password(password, user.password))
    if user is None or bcrypt.verify_password(password, user.password) is False:
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
    
    token = jwt.create_access_token(user.id, timedelta(minutes=60))
    
    access_data = AccessCreate(
        token=token,
        user_id=user.id,
        active=True
    )
    
    access = access_service.create(db, access_data)
    
    return {"access_token": token, "token_type": "Bearer"}


    
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido")

    user_id = int(payload.get("sub"))

    access = access_service.get_active_access_token(db, token)
    if not access:
        raise HTTPException(status_code=401, detail="Token inativo")

    user = user_service.get_by_id(db, access.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return user