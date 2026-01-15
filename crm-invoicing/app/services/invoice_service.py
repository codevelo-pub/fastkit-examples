from fastkit_core.services import AsyncBaseCrudService
from fastkit_core.database import AsyncRepository
from sqlalchemy.orm import Session
from app.models import Invoice, InvoiceItem
from app.schemas import InvoiceCreate, InvoiceUpdate, InvoiceResponse

class InvoiceService(AsyncBaseCrudService[Invoice, InvoiceCreate, InvoiceUpdate, InvoiceResponse]):
    def __init__(self, session: Session):
        self.repository = AsyncRepository(Invoice, session)
        self.invoice_item_repository = AsyncRepository(InvoiceItem, session)
        self.session = session
        super().__init__(self.repository, response_schema=InvoiceResponse)

    async def create_with_items(self, data: InvoiceCreate) -> InvoiceResponse:
        data_dict = data.model_dump()
        items_data = data_dict.pop('items', [])

        invoice = await self.repository.create(data=data_dict, commit=True)

        for item_data in items_data:
            item_data['invoice_id'] = invoice.id
            await self.invoice_item_repository.create(data=item_data, commit=True)

        await self.session.refresh(invoice, attribute_names=['items'])

        return InvoiceResponse.model_validate(invoice)
