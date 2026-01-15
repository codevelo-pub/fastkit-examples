from fastkit_core.services import AsyncBaseCrudService
from fastkit_core.database import AsyncRepository
from sqlalchemy.orm import Session
from app.models import Invoice
from app.schemas import InvoiceCreate, InvoiceUpdate, InvoiceResponse

class InvoiceService(AsyncBaseCrudService[Invoice, InvoiceCreate, InvoiceUpdate, InvoiceResponse]):
    def __init__(self, session: Session):
        repository = AsyncRepository(Invoice, session)
        super().__init__(repository, response_schema=InvoiceResponse)