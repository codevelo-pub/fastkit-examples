from fastapi import FastAPI, Depends
from fastkit_core.config import ConfigManager
from fastkit_core.database import init_database, get_db
from fastkit_core.http import success_response, paginated_response
from sqlalchemy.orm import Session
from models import Todo, TodoCreate, TodoUpdate, TodoResponse
from services import TodoService

# Initialize FastAPI
app = FastAPI(title="FastKit Quickstart API")

# Configure database
config = ConfigManager(modules=['database'], auto_load=True)
init_database(config)

# Create database tables
from fastkit_core.database import get_db_manager
Todo.metadata.create_all(get_db_manager().engine)


# Dependency injection
def get_todo_service(session: Session = Depends(get_db)) -> TodoService:
    return TodoService(session)

# API Endpoints
@app.post("/todos", status_code=201)
def create_todo(
    todo: TodoCreate,
    service: TodoService = Depends(get_todo_service)
):
    """Create a new todo."""
    created = service.create(todo.model_dump())
    return success_response(
        data=created.model_dump(),
        message="Todo created successfully"
    )


@app.get("/todos")
def list_todos(
        page: int = 1,
        per_page: int = 10,
        completed: bool | None = None,
        service: TodoService = Depends(get_todo_service)
):
    """List all todos with pagination."""
    filters = {}
    if completed is not None:
        filters["completed"] = completed

    todos, meta = service.paginate(
        page=page,
        per_page=per_page,
        **filters
    )
    return paginated_response(
        items=[t.model_dump() for t in todos],
        pagination=meta
    )


@app.get("/todos/{todo_id}")
def get_todo(
        todo_id: int,
        service: TodoService = Depends(get_todo_service)
):
    """Get a specific todo."""
    todo = service.find_or_fail(todo_id)
    return success_response(
        data=todo.model_dump()
    )


@app.put("/todos/{todo_id}")
def update_todo(
        todo_id: int,
        todo: TodoUpdate,
        service: TodoService = Depends(get_todo_service)
):
    """Update a todo."""
    updated = service.update(todo_id, todo.model_dump(exclude_unset=True))
    return success_response(
        data=updated.model_dump(),
        message="Todo updated successfully"
    )


@app.post("/todos/{todo_id}/complete")
def complete_todo(
        todo_id: int,
        service: TodoService = Depends(get_todo_service)
):
    """Mark todo as completed."""
    todo = service.mark_completed(todo_id)
    return success_response(
        data=todo.model_dump(),
        message="Todo marked as completed"
    )


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(
        todo_id: int,
        service: TodoService = Depends(get_todo_service)
):
    """Delete a todo."""
    service.delete(todo_id)


@app.get("/")
def root():
    """API root endpoint."""
    return {
        "message": "Welcome to FastKit Quickstart API!",
        "docs": "/docs"
    }