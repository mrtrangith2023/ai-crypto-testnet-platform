from sqlalchemy.orm import Session

from app.models.portfolio import Portfolio

from app.schemas.portfolio import (
    PortfolioCreate
)

from fastapi import HTTPException

from app.models.project import Project


def create_portfolio(
    db: Session,
    payload: PortfolioCreate,
    user_id: int
):

    portfolio = Portfolio(
        name=payload.name,
        user_id=user_id
    )

    db.add(portfolio)

    db.commit()

    db.refresh(portfolio)

    return portfolio


def get_portfolios(
    db: Session,
    user_id: int
):

    return db.query(
        Portfolio
    ).filter(
        Portfolio.user_id == user_id
    ).all()

def get_portfolio_stats(
    db,
    portfolio_id: int
):

    total = db.query(
        PortfolioProject
    ).filter(
        PortfolioProject.portfolio_id == portfolio_id
    ).count()

    return {
        "portfolio_id": portfolio_id,
        "total_projects": total
    }

def add_project_to_portfolio(
    db,
    portfolio_id: int,
    project_id: int
):

    project = db.query(
        Project
    ).filter(
        Project.id == project_id
    ).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    item = PortfolioProject(
        portfolio_id=portfolio_id,
        project_id=project_id
    )

    db.add(item)

    db.commit()

    db.refresh(item)

    return item

from app.models.portfolio_project import (
    PortfolioProject
)