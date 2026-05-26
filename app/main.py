from fastapi import FastAPI
from app.routes.wallet_routes import router

app = FastAPI(
    title="AI Crypto Testnet Platform"
)

app.include_router(router)