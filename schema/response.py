from pydantic import BaseModel

class TodoResponse(BaseModel): #Data return rule
    id: int
    title: str
    is_done: bool

