import jwt
import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv() #Load .env

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY") #Read Database Url from loaded .env

if not JWT_SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY 환경 변수가 설정되지 않았습니다.") #If it is not valid, raise error


ALGORITHM = "HS256" #Set Algorithm for en/decryption

def create_access_token(user_id: int, expires_minutes :int): #Creating Access Token
    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=expires_minutes),
    }

    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM)
