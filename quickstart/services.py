from fastkit_core.services import BaseCrudService
from fastkit_core.database import Repository
from models import Todo, TodoCreate, TodoUpdate
from sqlalchemy.orm import Session


class TodoService(BaseCrudService[Todo, TodoCreate, TodoUpdate]):
    """Service for Todo business logic."""

    def __init__(self, session: Session):
        repository = Repository(Todo, session)
        super().__init__(repository)

    def mark_completed(self, todo_id: int) -> Todo:
        """Mark a todo as completed."""
        return self.update(todo_id, {"completed": True})

    def mark_incomplete(self, todo_id: int) -> Todo:
        """Mark a todo as incomplete."""
        return self.update(todo_id, {"completed": False})