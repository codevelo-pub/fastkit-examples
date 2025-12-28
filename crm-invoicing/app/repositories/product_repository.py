from fastkit_core.database import Repository
from app.models.product import Product
from sqlalchemy.orm import Session

class ProductRepository(Repository):

    def __init__(self, model: Product, session: Session):
        super().__init__(model, session)
