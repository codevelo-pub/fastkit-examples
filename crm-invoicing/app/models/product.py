from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column
from fastkit_core.database import BaseWithTimestamps, SoftDeleteMixin, TranslatableMixin, IntIdMixin, SlugMixin

class Product(IntIdMixin, BaseWithTimestamps, SoftDeleteMixin, TranslatableMixin, SlugMixin):
    __tablename__ = "products"
    __translatable__ = ['name', 'description']

    sku: Mapped[str] = mapped_column(String(100), unique=True)
    name:  Mapped[dict] = mapped_column(JSON)
    description:  Mapped[dict] = mapped_column(JSON)
    price: Mapped[float] = mapped_column()


