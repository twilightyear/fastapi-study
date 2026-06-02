from pydantic import BaseModel

class TodoCreateRequest(BaseModel): #Data creation rule
    title: str
    is_done: bool = False


class TodoUpdateRequest(BaseModel): #Data update rule
    title: str | None = None
    is_done: bool | None = None

