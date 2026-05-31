from fastapi import APIRouter
from fastapi import Depends

from app.auth.dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)

@router.get("/")
def my_profile(
    current_user=Depends(
        get_current_user
    )
):
    return {
        "message": "Authenticated",
        "user": current_user
    }