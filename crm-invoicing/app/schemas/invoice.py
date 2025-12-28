from fastkit_core.validation import BaseSchema
from app.models.enums import InvoicesStatus
from app.schemas.invoice_item import InvoiceItemCreate, InvoiceItemResponse
from pydantic import Field
import datetime


class InvoiceCreate(BaseSchema):
    client_id: int = Field(gt=0, description="Client ID")
    items: list[InvoiceItemCreate] = Field(min_length=1, description="Invoice items (min: 1)")
    notes: str | None = Field(None, max_length=1000)

class InvoiceUpdate(BaseSchema):
    status: InvoicesStatus | None = None


class InvoiceResponse(BaseSchema):
    """Schema for invoice in responses."""
    id: int
    invoice_number: str
    client_id: int
    status: InvoicesStatus
    pdf_path: str | None
    created_at: datetime
    updated_at: datetime

    # Nested relationships (optional)
    items: list[InvoiceItemResponse] = []

    model_config = {"from_attributes": True}
