from fastkit_core.services import AsyncBaseCrudService
from fastkit_core.database import AsyncRepository
from sqlalchemy.orm import Session
from app.models import Product
from app.schemas import ProductCreate, ProductUpdate, ProductResponse

class ProductService(AsyncBaseCrudService[Product, ProductCreate, ProductUpdate, ProductResponse]):
    def __init__(self, session: Session):
        self.repository = AsyncRepository(Product, session)
        super().__init__(self.repository, response_schema=ProductResponse)

    async def before_create(self, data: dict) -> dict:
        product = Product(**data)
        product.generate_slug(source_field='name')
        data['slug'] = product.slug

        return data

    def find_active(self) -> list[Product]:
        """Get all active products."""
        return self.filter(is_active=True, _order_by='name')

    def deactivate(self, product_id: int) -> Product:
        """Deactivate product (soft disable without deleting)."""
        return self.update(product_id, {'is_active': False})

    def activate(self, product_id: int) -> Product:
        """Activate product."""
        return self.update(product_id, {'is_active': True})

    def find_by_sku(self, sku: str) -> Product | None:
        """Find product by SKU."""
        return self.filter_one(sku=sku)
