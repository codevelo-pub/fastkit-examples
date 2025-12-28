from fastkit_core.validation import BaseSchema

class ProductCreate(BaseSchema):
    sku: str
    name: dict
    description: dict
    price: float
    stock: int
    is_active: bool

class ProductUpdate(ProductCreate):
    pass
