from fastkit_core.validation import BaseSchema
from app.models.enums import InvoicesStatus

class InvoiceCreate(BaseSchema):
    client_id: int
    status: InvoicesStatus

class InvoiceUpdate(InvoiceCreate):
    pass
