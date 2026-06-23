from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.auth.dependencies import (
    get_current_user
)

from app.services.xp_service import (
    get_user_xp,
    get_leaderboard,
    get_user_rank
)

router = APIRouter(
    prefix="/xp",
    tags=["XP"]
)

@router.get("/me")
def my_xp(
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return get_user_xp(
        db,
        int(current_user["sub"])
    )

@router.get("/leaderboard")
def leaderboard(
    db: Session = Depends(get_db)
):

    return get_leaderboard(db)

@router.get("/rank")
def my_rank(
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return get_user_rank(
        db,
        int(current_user["sub"])
    )

