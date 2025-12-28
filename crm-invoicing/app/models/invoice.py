from typing import Optional
from fastkit_core.database import BaseWithTimestamps, SoftDeleteMixin, IntIdMixin
from sqlalchemy import String, Column, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.enums import InvoicesStatus
from app.models.client import Client

class Invoice(IntIdMixin, BaseWithTimestamps, SoftDeleteMixin):
    __tablename__ = "invoices"

    invoice_number: Mapped[str] = mapped_column(String(20), unique=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    pdf_path: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    status = Column(Enum(InvoicesStatus, name="status"), nullable=False)

    client: Mapped["Client"] = relationship(back_populates="invoices")
