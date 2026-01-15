from fastkit_core.validation import BaseSchema
from pydantic import Field

class InvoiceItemCreate(BaseSchema):
    product_id: int = Field(gt=0, description="Product ID")
    quantity: int = Field(default=1, ge=1, description="Quantity (min: 1)")
    unit_price: float =  Field(gt=0, description="Unit Price")

class InvoiceItemUpdate(BaseSchema):
    quantity: int | None = Field(None, ge=1)
    unit_price: float | None = Field(None, gt=0)

class InvoiceItemResponse(BaseSchema):
    id: int
    invoice_id: int
    product_id: int
    quantity: int
    unit_price: float

    model_config = {"from_attributes": True}
