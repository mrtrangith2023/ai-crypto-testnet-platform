from fastapi import APIRouter
from fastapi import Depends

from app.auth.dependencies import (
    get_current_user
)

router = APIRouter(
    tags=["Profile"]
)


@router.get("/profile/")
def profile(
    user=Depends(get_current_user)
):
    return {
        "message": "Authenticated",
        "user": user
    }