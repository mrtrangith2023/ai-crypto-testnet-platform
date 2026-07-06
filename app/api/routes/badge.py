from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.auth.dependencies import get_current_user

from app.schemas.badge import (
    BadgeCreate,
    BadgeResponse,
    MyBadgeResponse
)

from app.services.badge_service import (
    create_badge,
    get_badges,
    get_my_badge
)

router = APIRouter(
    prefix="/badges",
    tags=["Badges"]
)

@router.post(
    "/",
    response_model=BadgeResponse
)
def create_new_badge(
    payload: BadgeCreate,
    db: Session = Depends(get_db)
):

    return create_badge(
        db,
        payload.name,
        payload.xp_required
    )

@router.get(
    "/",
    response_model=list[BadgeResponse]
)
def list_badges(
    db: Session = Depends(get_db)
):

    return get_badges(db)

@router.get(
    "/me",
    response_model=MyBadgeResponse
)
def my_badge(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_my_badge(
        db,
        int(current_user["sub"])
    )