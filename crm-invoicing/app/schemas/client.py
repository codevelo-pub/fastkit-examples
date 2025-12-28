from typing import Optional

from fastkit_core.validation import BaseSchema
from app.models.enums import Languages

class ClientCreate(BaseSchema):
    name: str
    description: Optional[str] = None
    language: Languages
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None

class ClientUpdate(ClientCreate):
    pass
