from fastkit_core.services import BaseCrudService
from fastkit_core.database import Repository
from sqlalchemy.orm import Session
from app.models import Product
from app.schemas import ProductCreate, ProductUpdate

class ProductService(BaseCrudService[Product, ProductCreate, ProductUpdate]):
    def __init__(self, session: Session):
        repository = Repository(Product, session)
        super().__init__(repository)