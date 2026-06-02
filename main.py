from fastapi import FastAPI
from database.db_connection import engine
from database.orm import Base
from routers.todo import router as todos_router

Base.metadata.create_all(bind=engine) #Create database using "Base" and SQLAlchemy


app = FastAPI() #Create Fast-api Object
app.include_router(todos_router)
