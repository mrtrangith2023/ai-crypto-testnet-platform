from fastapi import APIRouter
from fastapi import Depends

from app.auth.roles import (
    require_role
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/dashboard")
def admin_dashboard(
    current_user=Depends(
        require_role(["admin"])
    )
):
    return {
        "message": "Welcome Admin",
        "user": current_user
    }