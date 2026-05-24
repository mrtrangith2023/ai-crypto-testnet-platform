from fastapi import APIRouter

from app.api.routes import health
from app.api.routes import wallet

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(wallet.router)