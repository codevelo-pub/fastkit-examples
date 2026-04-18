from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON, String, Numeric
from fastkit_core.database import (
    BaseWithTimestamps,
    IntIdMixin,
    # UUIDMixin,          # Uncomment to use UUID as primary key instead of IntIdMixin
    SoftDeleteMixin,    # Uncomment to enable soft delete (deleted_at)
    SlugMixin,          # Uncomment to add slug field (slug)
    # PublishableMixin,   # Uncomment to add published_at field
    TranslatableMixin,  # Uncomment for multi-language field support
)


class Product(IntIdMixin, BaseWithTimestamps, SoftDeleteMixin, TranslatableMixin, SlugMixin):
    __tablename__ = "products"
    __translatable__ = ['name', 'description']

    sku: Mapped[str] = mapped_column(String(100), unique=True)
    name: Mapped[dict] = mapped_column(JSON)
    description: Mapped[dict] = mapped_column(JSON)
    price: Mapped[float] = mapped_column(Numeric(10, 2))
    stock: Mapped[int] = mapped_column(default=0)
    is_active: Mapped[bool] = mapped_column(default=True)