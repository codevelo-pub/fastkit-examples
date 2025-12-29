from fastkit_core.services import BaseCrudService
from fastkit_core.database import Repository
from sqlalchemy.orm import Session
from app.models import InvoiceItem
from app.schemas import InvoiceItemCreate, InvoiceItemUpdate

class InvoiceItemService(BaseCrudService[InvoiceItem, InvoiceItemCreate, InvoiceItemUpdate]):
    def __init__(self, session: Session):
        repository = Repository(InvoiceItem, session)
        super().__init__(repository)