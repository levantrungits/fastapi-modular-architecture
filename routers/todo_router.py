from fastapi import APIRouter
from handlers.todo_handler import TodoHandler, TodoCreate, Todo

router = APIRouter()
todo_handler = TodoHandler()

@router.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    return todo_handler.create_todo(todo)

@router.get("/todos", response_model=list[Todo])
def get_todos():
    return todo_handler.get_todos()

@router.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    return todo_handler.get_todo(todo_id)

@router.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoCreate):
    return todo_handler.update_todo(todo_id, updated_todo)

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    return todo_handler.delete_todo(todo_id)
