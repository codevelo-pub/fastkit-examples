from fastkit_core.database import Repository
from app.models.invoice import Invoice
from sqlalchemy.orm import Session

class InvoiceRepository(Repository):

    def __init__(self, model: Invoice, session: Session):
        super().__init__(model, session)
