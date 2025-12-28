from fastkit_core.database import Repository
from app.models.client import Client
from sqlalchemy.orm import Session

class ClientRepository(Repository):

    def __init__(self, model: Client, session: Session):
        super().__init__(model, session)
