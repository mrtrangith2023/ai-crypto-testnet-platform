from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.auth.dependencies import get_current_user

from app.schemas.watchlist import (
    WatchlistCreate,
    WatchlistResponse
)

from app.services.watchlist_service import (
    add_watchlist,
    get_watchlist
)

router = APIRouter(
    prefix="/watchlist",
    tags=["Watchlist"]
)

@router.post(
    "/",
    response_model=WatchlistResponse
)
def create_watchlist(
    payload: WatchlistCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):
    return add_watchlist(
        db,
        int(current_user["sub"]),
        payload
    )


@router.get(
    "/",
    response_model=list[WatchlistResponse]
)
def get_my_watchlist(
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):
    return get_watchlist(
        db,
        int(current_user["sub"])
    )