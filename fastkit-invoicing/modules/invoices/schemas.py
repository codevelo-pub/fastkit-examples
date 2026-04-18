from typing import Any
from pydantic import Field
from app.models.enums import InvoicesStatus
from fastkit_core.validation import (
    BaseSchema,
    BaseCreateSchema,
    BaseUpdateSchema
)


class InvoiceCreate(BaseCreateSchema):
    client_id: int = Field(gt=0, description="Client ID")
    invoice_number: str


class InvoiceUpdate(BaseUpdateSchema):
    status: InvoicesStatus | None = None


class InvoiceResponse(BaseSchema):
    """
    Schema for Invoice API responses.

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
