import jwt
import datetime
import os

SECRET_KEY = os.getenv('SECRET_KEY_JWT')

def create_access_token(user_id: int, expires_delta: datetime.timedelta = None):
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)

    to_encode = {"exp": expire, "sub": str(user_id)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt