from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.auth.dependencies import (
    get_current_user
)

from app.schemas.portfolio import (
    PortfolioCreate,
    PortfolioResponse
)

from app.services.portfolio_service import (
    create_portfolio,
    get_portfolios
)

from app.schemas.portfolio_project import (
    PortfolioProjectCreate,
    PortfolioProjectResponse
)
from app.services.portfolio_service import (
    add_project_to_portfolio,
    get_portfolio_stats
)

router = APIRouter(
    prefix="/portfolios",
    tags=["Portfolios"]
)


@router.post(
    "/",
    response_model=PortfolioResponse
)
def create_new_portfolio(
    payload: PortfolioCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return create_portfolio(
        db,
        payload,
        int(current_user["sub"])
    )


@router.get(
    "/",
    response_model=list[PortfolioResponse]
)
def get_my_portfolios(
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return get_portfolios(
        db,
        int(current_user["sub"])
    )

@router.post(
    "/{portfolio_id}/projects",
    response_model=PortfolioProjectResponse
)
def add_project(
    portfolio_id: int,
    payload: PortfolioProjectCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return add_project_to_portfolio(
        db,
        portfolio_id,
        payload.project_id
    )

@router.get(
    "/{portfolio_id}/stats"
)
def portfolio_stats(
    portfolio_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return get_portfolio_stats(
        db,
        portfolio_id
    )