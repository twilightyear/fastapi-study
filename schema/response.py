from datetime import datetime
from pydantic import BaseModel

class TodoResponse(BaseModel): #Todo data return rule
    id: int
    title: str
    is_done: bool

class UserSignUpResponse(BaseModel): #User Data return rule
    id: int
    email: str
    created_at: datetime
