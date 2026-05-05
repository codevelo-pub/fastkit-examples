from fastapi import FastAPI
from modules.clients.router import router as clients_router
from modules.products.router import router as products_router
from modules.invoices.router import router as invoices_router

from fastkit_core.database import init_async_database
from fastkit_core.cache import setup_cache, get_cache
from fastkit_core.config import ConfigManager
from fastkit_core.http import create_health_router, HealthCheck
import time

configuration = ConfigManager(modules=['app', 'database', 'cache'])
init_async_database(configuration)
setup_cache(configuration)


async def redis_check() -> HealthCheck:
    start = time.monotonic()
    try:
        cache = get_cache()
        await cache.set('__health__', '1', ttl=5)
        latency_ms = int((time.monotonic() - start) * 1000)
        return HealthCheck(name='redis', status='ok', latency_ms=latency_ms)
    except Exception as e:
        latency_ms = int((time.monotonic() - start) * 1000)
        return HealthCheck(name='redis', status='error', detail=str(e), latency_ms=latency_ms)


app = FastAPI()

app.include_router(
    create_health_router(checks=[redis_check]),
    prefix='/health',
    tags=['Health'],
)
app.include_router(clients_router)
app.include_router(products_router)
app.include_router(invoices_router)