from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.database import Base


class Reward(Base):
    __tablename__ = "rewards"

    id = Column(
        Integer,
        primary_key=True
    )

    campaign_id = Column(
        Integer,
        ForeignKey("campaigns.id")
    )

    name = Column(
        String
    )

    xp = Column(
        Integer
    )