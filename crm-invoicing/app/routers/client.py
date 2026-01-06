from fastapi import APIRouter, Depends
from app.infrastructure.auth import current_active_user
from fastkit_core.http import success_response, paginated_response
from fastkit_core.database import get_async_db
from fastkit_core.i18n import _
from sqlalchemy.orm import Session
from app.models import Client
from starlette.responses import JSONResponse
from app.schemas import ClientCreate, ClientUpdate
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
    clients, meta = await service.paginate(page=page, per_page=per_page)
    return paginated_response(items=clients, pagination=meta)

@router.post('', name='api.clients.store')
async def store(client: ClientCreate, service: ClientService = Depends(get_service)):
    data = await service.create(client.model_dump())
    return success_response(
        data= data.model_dump(),
        message=_('clients.create'),
        status_code=201
    )
