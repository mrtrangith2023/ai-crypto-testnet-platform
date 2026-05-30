from fastapi import FastAPI

from app.database.database import engine, Base
from app.routes.user_routes import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Crypto Testnet Platform",
    version="0.1.0"
)

app.include_router(user_router)