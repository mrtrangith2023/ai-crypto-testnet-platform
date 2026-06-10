from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from app.database.database import Base

class Watchlist(Base):

    __tablename__ = "watchlists"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    project_id = Column(
        Integer,
        ForeignKey("projects.id")
    )