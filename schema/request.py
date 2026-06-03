import re
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError


class TodoCreateRequest(BaseModel): #Data creation rule
    title: str
    is_done: bool = False


class TodoUpdateRequest(BaseModel): #Data update rule
    title: str | None = None
    is_done: bool | None = None


class UserSignUpRequest(BaseModel): #Sign up rule
    email: EmailStr = Field(..., description="Email address")
    password: str = Field(..., min_length=8, description="Password")

    #Rule for password field : It must contain least one upper&lowercase eng, num and special char.
    @field_validator("password")
    def validate_password(cls, value):
        if not re.search(r"[A-Z]",value):
            raise ValueError("Password must contain least one uppercase letter")
        if not re.search(r"[a-z]",value):
            raise ValueError("Password must contain least one lowercase letter.")
        if not re.search(r"[0-9]",value):
            raise ValueError("Password must contain least one number")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>_]",value):
            raise ValueError("Password must contain least one special character")
        return value
