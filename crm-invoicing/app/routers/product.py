from fastapi import APIRouter, Depends
from app.infrastructure.auth import current_active_user
from fastkit_core.http import success_response, paginated_response
from fastkit_core.database import get_async_db
from fastkit_core.i18n import _
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from app.schemas import ProductCreate, ProductUpdate
from app.services import ProductService

router = APIRouter(
    prefix='/products',
    tags=['Products'],
    dependencies=[Depends(current_active_user)]
)

def get_service(session: Session = Depends(get_async_db)) -> ProductService:
    return ProductService(session)

@router.get('', name='api.products.index')
async def index(
        page: int = 1,
        per_page: int = 10,
        service: ProductService = Depends(get_service)
) -> JSONResponse:
    products, meta = await service.paginate(page=page, per_page=per_page)
    return paginated_response(items=[product.model_dump() for product in products], pagination=meta)
