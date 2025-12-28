from sqlalchemy import String, Column, Enum
from sqlalchemy.orm import Mapped, mapped_column
from fastkit_core.database import BaseWithTimestamps, SoftDeleteMixin, IntIdMixin
from app.models.enums import Languages

class Client(IntIdMixin, BaseWithTimestamps, SoftDeleteMixin):
    __tablename__ = "clients"

    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] =  mapped_column(String(255))
    language = Column(Enum(Languages, name="language"), nullable=False)
