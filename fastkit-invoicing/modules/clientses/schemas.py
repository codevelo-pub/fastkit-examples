from typing import Any
from pydantic import Field, EmailStr
from fastkit_core.validation import (
    BaseSchema,
    BaseCreateSchema,
    BaseUpdateSchema
)
from app.models.enums import Languages


class ClientsCreate(BaseCreateSchema):
    name: str = Field(min_length=1, max_length=255)
    description: str | None = Field(None, max_length=255)
    language: Languages = Field(default=Languages.EN)

    email: EmailStr | None = None
    phone: str | None = Field(None, max_length=50)

    address: str | None = Field(None, max_length=500)
    city: str | None = Field(None, max_length=100)
    country: str | None = Field(None, max_length=100)
    postal_code: str | None = Field(None, max_length=20)


class ClientsUpdate(BaseUpdateSchema):
    """
    Schema for updating an existing Clients.

    All fields should be optional (| None = None) to support partial updates.

    Example:
        name: str | None = None
        price: float | None = None
    """
    pass  # Replace with actual fields


class ClientsResponse(BaseSchema):
    """
    Schema for Clients API responses.

    Include all fields that should be returned to the client.
    Always include id and timestamps from BaseWithTimestamps.

    model_config from_attributes=True is required for SQLAlchemy model mapping.
    """
    id: int
    # Add your fields here
    # Example:
    # name: str
    # price: float
    # description: str | None = None
    created_at: Any = None
    updated_at: Any = None
