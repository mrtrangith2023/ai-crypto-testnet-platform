from fastapi import APIRouter

from app.api.routes import health
from app.api.routes import wallet
from app.api.routes import user
from app.api.routes import auth
from app.api.routes import profile

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(wallet.router)
api_router.include_router(profile.router)
api_router.include_router(auth.router)
api_router.include_router(user.router)