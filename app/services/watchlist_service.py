from sqlalchemy.orm import Session

from app.models.watchlist import Watchlist

from app.schemas.watchlist import (
    WatchlistCreate
)

def add_watchlist(
    db: Session,
    user_id: int,
    payload: WatchlistCreate
):

    item = Watchlist(
        user_id=user_id,
        project_id=payload.project_id
    )

    db.add(item)

    db.commit()

    db.refresh(item)

    return item

def get_watchlist(
    db: Session,
    user_id: int
):

    return db.query(
        Watchlist
    ).filter(
        Watchlist.user_id == user_id
    ).all()