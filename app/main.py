from fastapi import FastAPI

from app.database.database import engine, Base

from app.routes.user_routes import router as user_router
from app.routes.auth_routes import router as auth_router
from app.routes.profile_routes import (
    router as profile_router
)
from app.api.routes.wallet import router as wallet_router

from app.models.project import Project

from app.api.routes.project import (
    router as project_router
)

from app.models.watchlist import Watchlist
from app.api.routes.watchlist import (
    router as watchlist_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Crypto Testnet Platform",
    version="0.1.0"
)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(wallet_router)
app.include_router(project_router)
app.include_router(watchlist_router)