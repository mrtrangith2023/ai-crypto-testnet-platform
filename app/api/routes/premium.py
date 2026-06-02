from fastapi import APIRouter
from fastapi import Depends

from app.auth.roles import (
    require_role
)

router = APIRouter(
    prefix="/premium",
    tags=["Premium"]
)

@router.get("/ai-score")
def ai_score_feature(
    current_user=Depends(
        require_role(
            [
                "premium",
                "admin"
            ]
        )
    )
):
    return {
        "message":
        "AI Scoring Feature"
    }