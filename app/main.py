from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="AI Crypto Testnet Platform",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "AI Crypto Testnet Platform Running"
    }