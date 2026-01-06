from fastapi import APIRouter, Depends
from app.infrastructure.auth import current_active_user
from fastkit_core.http import success_response, paginated_response
from fastkit_core.database import get_async_db
from sqlalchemy.orm import Session
from app.models import Client
from starlette.responses import JSONResponse
from app.schemas import ClientCreate, ClientUpdate, ClientResponse
from app.services import ClientService

router = APIRouter(
    prefix='/clients',
    tags=['Clients'],
    dependencies=[Depends(current_active_user)]
)

def get_service(session: Session = Depends(get_async_db)) -> ClientService:
    return ClientService(session)

@router.get('', name='api.clients.index')
async def index(
        page: int = 1,
        per_page: int = 10,
        service: ClientService = Depends(get_service)
) -> JSONResponse:

    clients, meta = service.paginate(page=page, per_page=per_page)

    return paginated_response(
        items= [ClientResponse.from_orm(c).model_dump() for c in clients],
        pagination=meta
    )
