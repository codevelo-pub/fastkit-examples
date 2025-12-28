from fastkit_core.database import Repository
from app.models.invoice_item import InvoiceItem
from sqlalchemy.orm import Session

class InvoiceItemRepository(Repository):

    def __init__(self, model: InvoiceItem, session: Session):
        super().__init__(model, session)
