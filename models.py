from datetime import datetime
from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.orm import Base

class Todo(Base): #Table of to-do-list
    __tablename__ = 'todo'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True #automatic id increment
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False #null not available
    )

    is_done: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False, #null not available
        default=False #set to False if it is empty
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'), #It is linked to Table of user
        nullable=True #null is available
    )

    user: Mapped["User"] = relationship(
        back_populates="todos" #Setting Relationship with Table of user for our ease(Object Link)
    )


class User(Base): #Table of user
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(), #time now
        nullable=False
    )

    todos: Mapped[list["Todo"]] = relationship(
        back_populates="user", #Setting Relationship with Table of to-do-list for our ease(Object Link)
        cascade="all, delete-orphan" #Cascade delete
    )
