import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv() #Load .env

DATABASE_URL = os.getenv("DATABASE_URL") #Read Database Url from loaded .env

if not DATABASE_URL:
    raise ValueError("DATABASE_URL 환경 변수가 설정되지 않았습니다.") #If it is not valid, raise error

engine = create_engine(DATABASE_URL, echo=True) #Create terminal-loggable SQLAlchemy DB Engine.

SessionFactory = sessionmaker( #Create Session Factory
    autocommit=False, #Ensure Integrity and Transaction
    autoflush=False, #Prevent Unpredictable Query
    expire_on_commit=False,
    bind=engine, #Bind with SQLAlchemy DB Engine
)
