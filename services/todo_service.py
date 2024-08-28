from repositories.todo_repository import TodoRepository, TodoCreate, Todo

class TodoService:
    def __init__(self):
        self.todo_repo = TodoRepository()
    
    def create_todo(self, todo: TodoCreate) -> Todo:
        return self.todo_repo.create_todo(todo)
    
    def get_todos(self) -> list[Todo]:
        return self.todo_repo.get_todos()
    
    def get_todo(self, todo_id: int) -> Todo | None:
        return self.todo_repo.get_todo(todo_id)
    
    def update_todo(self, todo_id: int, updated_todo: TodoCreate) -> Todo | None:
        return self.todo_repo.update_todo(todo_id, updated_todo)
    
    def delete_todo(self, todo_id: int) -> bool:
        return self.todo_repo.delete_todo(todo_id)