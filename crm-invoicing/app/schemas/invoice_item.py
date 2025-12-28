from fastkit_core.validation import BaseSchema

class InvoiceItemCreate(BaseSchema):
    invoice_id: int
    product_id: int
    quantity: int
    unit_price: float

class InvoiceItemUpdate(InvoiceItemCreate):
    pass
