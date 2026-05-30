from fastapi import APIRouter
# app/api/routes/health.py

from app.core.config import SECRET_KEY

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "success",
        "secret_loaded": bool(SECRET_KEY)
    }