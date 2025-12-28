from datetime import datetime

from fastkit_core.validation import BaseSchema
from fastkit_core.i18n import _
from pydantic import Field, field_validator


class ProductCreate(BaseSchema):
    """Schema for creating a product."""
    sku: str = Field(min_length=1, max_length=100, description="Product SKU (unique)")
    name: dict[str, str] = Field(description="Translated product names")
    description: dict[str, str] = Field(default_factory=dict, description="Translated descriptions")
    price: float = Field(gt=0, description="Price (must be positive)")
    stock: int = Field(default=0, ge=0, description="Stock quantity")

    @field_validator('name')
    @classmethod
    def validate_name(cls, v: dict[str, str]) -> dict[str, str]:
        """Ensure at least English name exists."""
        if not v:
            raise ValueError(_("validation.product.name.required"))
        if 'en' not in v:
            raise ValueError(_("validation.product.name.english_required"))
        return v

    @field_validator('name', 'description')
    @classmethod
    def validate_translation_keys(cls, v: dict[str, str]) -> dict[str, str]:
        """Validate language keys are valid ISO codes."""
        valid_langs = {'en', 'de', 'es'}  # Match your Languages enum
        for key in v.keys():
            if key not in valid_langs:
                raise ValueError(_("validation.product.invalid_language_code", None, **{'key': key, 'valid_langs': valid_langs}))
        return v


class ProductUpdate(BaseSchema):
    """Schema for updating a product."""
    sku: str | None = Field(None, min_length=1, max_length=100)
    name: dict[str, str] | None = None
    description: dict[str, str] | None = None
    price: float | None = Field(None, gt=0)
    stock: int | None = Field(None, ge=0)
    is_active: bool | None = None


class ProductResponse(BaseSchema):
    """Schema for product in responses."""
    id: int
    sku: str
    slug: str
    name: dict[str, str]
    description: dict[str, str]
    price: float
    stock: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}