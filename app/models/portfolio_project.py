from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from app.database.database import Base


class PortfolioProject(Base):
    __tablename__ = "portfolio_projects"

    id = Column(
        Integer,
        primary_key=True
    )

    portfolio_id = Column(
        Integer,
        ForeignKey("portfolios.id")
    )

    project_id = Column(
        Integer,
        ForeignKey("projects.id")
    )