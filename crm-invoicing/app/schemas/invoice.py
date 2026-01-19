from fastkit_core.validation import BaseSchema
from app.models.enums import InvoicesStatus
from app.schemas.invoice_item import InvoiceItemCreate, InvoiceItemResponse
from pydantic import Field, computed_field


class InvoiceCreate(BaseSchema):
    client_id: int = Field(gt=0, description="Client ID")
    items: list[InvoiceItemCreate] = Field(min_length=1, description="Invoice items (min: 1)")
    invoice_number: str

class InvoiceUpdate(BaseSchema):
    status: InvoicesStatus | None = None


class InvoiceResponse(BaseSchema):
    """Schema for invoice in responses."""
    id: int
    invoice_number: str
    client_id: int
    status: InvoicesStatus
    pdf_path: str | None

    # Nested relationships (optional)
    items: list[InvoiceItemResponse] = []

    model_config = {"from_attributes": True}

    @computed_field
    @property
    def total_amount(self) -> float:
        return sum(item.quantity * item.unit_price for item in self.items)