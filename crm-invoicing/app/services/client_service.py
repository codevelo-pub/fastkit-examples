from fastkit_core.services import BaseCrudService
from fastkit_core.database import AsyncRepository
from sqlalchemy.orm import Session
from app.models import Client
from app.schemas import ClientCreate, ClientUpdate

class ClientService(BaseCrudService[Client, ClientCreate, ClientUpdate]):
    def __init__(self, session: Session):
        repository = AsyncRepository(Client, session)
        super().__init__(repository)