from typing import Any
from pydantic import Field
from fastkit_core.validation import (
    BaseSchema,
    BaseCreateSchema,
    BaseUpdateSchema
)

# Translatable fields are stored as {"en": "...", "de": "...", "es": "..."}
TranslatableField = dict[str, str]


class ProductCreate(BaseCreateSchema):
    sku: str = Field(min_length=1, max_length=100, description="Product SKU (unique)")
    name: TranslatableField = Field(description="Translated product names e.g. {'en': 'Name', 'de': 'Name'}")
    description: TranslatableField = Field(default_factory=dict, description="Translated descriptions")
    price: float = Field(gt=0, description="Price (must be positive)")
    stock: int = Field(default=0, ge=0, description="Stock quantity")


class ProductUpdate(BaseUpdateSchema):
    sku: str | None = Field(None, min_length=1, max_length=100)
    name: TranslatableField | None = None
    description: TranslatableField | None = None
    price: float | None = Field(None, gt=0)
    stock: int | None = Field(None, ge=0)
    is_active: bool | None = None


class ProductResponse(BaseSchema):
    id: int
    sku: str
    slug: str
    name: TranslatableField
    description: TranslatableField
    price: float
    stock: int
    is_active: bool

    model_config = {"from_attributes": True}
