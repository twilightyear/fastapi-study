from fastapi import APIRouter, status, HTTPException
from sqlalchemy import select
from schema.request import UserSignUpRequest
from database.db_connection import SessionFactory
from models import User
from auth.password import hash_password
from schema.response import UserSignUpResponse

router = APIRouter(tags=["User"]) #API Wrapping group, function on User

@router.post(
    "/users/signup",
    status_code=status.HTTP_201_CREATED, #On success
    response_model=UserSignUpResponse #Response frame
)

def signup_user_handler(body: UserSignUpRequest):

    with SessionFactory() as session: #Start database session

        stmt = select(User).where(User.email == body.email)
        existing_user = session.scalar(stmt)
        if existing_user: #Check if it has same email on the db
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )

        hashed_password = hash_password(body.password) #Use hashed password for security

        user = User( #Create instance for db to save
            email=body.email,
            hashed_password=hashed_password,
        )


        session.add(user) #Add to the session
        session.commit() #Save

        session.refresh(user) #Refresh db
        return user
