from fastkit_core.database import Base, IntIdMixin, TimestampMixin
from fastkit_core.validation import BaseSchema
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean


# Database Model
class Todo(Base, IntIdMixin, TimestampMixin):
    """Todo database model with auto ID and timestamps."""
    __tablename__ = 'todos'

    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)


# Validation Schemas
class TodoCreate(BaseSchema):
    """Schema for creating a todo."""
    title: str
    description: str | None = None


class TodoUpdate(BaseSchema):
    """Schema for updating a todo."""
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


class TodoResponse(BaseSchema):
    """Schema for todo responses."""
    id: int
    title: str
    description: str | None
    completed: bool

    model_config = {"from_attributes": True}