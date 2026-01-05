from fastapi import FastAPI
from app.routers.auth import router as auth_router
from fastkit_core.database import init_async_database
from fastkit_core.config import ConfigManager
configuration = ConfigManager(modules=['app', 'database', 'auth'])
init_async_database(configuration)

app = FastAPI()
app.include_router(auth_router)
