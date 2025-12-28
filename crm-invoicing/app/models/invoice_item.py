from sqlalchemy.orm import Mapped, mapped_column, mapped_column, relationship
from sqlalchemy import Float, ForeignKey
from fastkit_core.database import Base, IntIdMixin
from app.models.invoice import Invoice
from app.models.product import Product

class InvoiceItem(IntIdMixin, Base):
    __tablename__ = "invoice_items"

    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int] = mapped_column(default=1)
    unit_price: Mapped[float] = mapped_column(Float)

    invoice: Mapped["Invoice"] = relationship(back_populates="items")
    product: Mapped["Product"] = relationship(back_populates="invoice_items")
