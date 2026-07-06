from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.database import Base


class Badge(Base):
    __tablename__ = "badges"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
        nullable=False
    )

    xp_required = Column(
        Integer,
        nullable=False
    )