from fastapi import HTTPException, APIRouter
from sqlalchemy import select
from starlette import status
from database.db_connection import SessionFactory
from models import Todo
from schema.request import TodoCreateRequest, TodoUpdateRequest
from schema.response import TodoResponse

router = APIRouter(tags=["Todo"])

@router.get(
    "/todos",
    response_model=list[TodoResponse], #specify form of response
    status_code=status.HTTP_200_OK #status code when it is well-returned
)
def get_todos_handler():
    session = SessionFactory() #Create Session to communicate with DB
    try:
        stmt = select(Todo) #statement "select" using Table of to-do-list
        todos = session.execute(stmt).scalars().all() #SELECT * FROM to-do-list
        return todos
    finally:
        session.close() #Close session


@router.get(
    "/todos/{todo_id}",
    response_model=TodoResponse, #specify form of response
    status_code=status.HTTP_200_OK #status code when it is well-returned
)
def get_todo_handler(todo_id: int):
    session = SessionFactory() #Create Session to communicate with DB
    try:
        stmt = select(Todo).where(Todo.id==todo_id) #Statement "select" using Table of to-do-list with condition
        todo = session.execute(stmt).scalars().first() #SELECT * FROM to-do-list WHERE Todo.id=todo_id LIMIT 1
        if todo: #If it exists
            return todo
        raise HTTPException( #If it does not exist
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    finally:
        session.close() #Close session


@router.post(
    "/todos",
    response_model=TodoResponse, #Specify form of response
    status_code=status.HTTP_201_CREATED  #Status code when it is well-created
)
def create_todo_handler(body: TodoCreateRequest):
    session = SessionFactory() #Create Session to communicate with DB
    try: #If it exists
        todo = Todo(
            title=body.title, #Get title that has been sent
            is_done=body.is_done, #Get is_done value that has been sent
        )
        session.add(todo) #Add to session
        session.commit() #Commit data
        return todo
    finally:
        session.close() #Close session


@router.patch(
    "/todos/{todo_id}",
    response_model=TodoResponse, #specify form of response
    status_code=status.HTTP_200_OK #status code when it is well-updated
)

def update_todo_handler(todo_id: int, body: TodoUpdateRequest):
    session = SessionFactory() #Create Session to communicate with DB
    try: #If it exists
        stmt = select(Todo).where(Todo.id==todo_id) #Statement "select" using Table of to-do-list with condition
        todo = session.execute(stmt).scalars().first() #SELECT * FROM to-do-list WHERE Todo.id=todo_id LIMIT 1
        if todo:
            if body.title is not None: #If sent title is empty
                todo.title = body.title
            if body.is_done is not None: #If sent .is_done is empty
                todo.is_done = body.is_done
            session.commit() #Commit
            return todo
        raise HTTPException( #Raise Exception if todo does not exist
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    finally:
        session.close() #Close session


@router.delete(
    "/todos/{todo_id}",
    status_code=status.HTTP_204_NO_CONTENT #status code when it is well-deleted
)

def delete_todo_handler(todo_id: int):
    session = SessionFactory() #Create Session to communicate with DB
    try: #If it exists
        stmt = select(Todo).where(Todo.id==todo_id) #Statement "select" using Table of to-do-list with condition
        todo = session.execute(stmt).scalars().first() #SELECT * FROM to-do-list WHERE Todo.id=todo_id LIMIT 1
        if todo:
            session.delete(todo) #Delete from session
            session.commit() #Commit
            return
        raise HTTPException( #Raise Exception if it is not found.
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo no found"
        )
    finally:
        session.close() #Close session
