from pydantic import Field, model_validator, computed_field
from typing import Optional
from fastkit_core.validation import (
    BaseSchema,
    BaseCreateSchema,
    BaseUpdateSchema,
)

class InvoiceItemCreate(BaseCreateSchema):
    product_id: int = Field(gt=0, description="Product ID")
    quantity: int = Field(default=1, ge=1, description="Quantity (min: 1)")
    unit_price: float =  Field(gt=0, description="Unit Price")


class InvoiceItemUpdate(BaseUpdateSchema):
    quantity: int | None = Field(None, ge=1)
    unit_price: float | None = Field(None, gt=0)


class InvoiceItemResponse(BaseSchema):
    """
    Schema for InvoiceItem API responses.

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
