from fastkit_core.services import BaseCrudService
from fastkit_core.database import Repository
from sqlalchemy.orm import Session
from app.models import Invoice
from app.schemas import InvoiceCreate, InvoiceUpdate

class InvoiceService(BaseCrudService[Invoice, InvoiceCreate, InvoiceUpdate]):
    def __init__(self, session: Session):
        repository = Repository(Invoice, session)
        super().__init__(repository)