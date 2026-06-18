from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from app.database.database import Base


class UserReward(Base):
    __tablename__ = "user_rewards"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    reward_id = Column(
        Integer,
        ForeignKey("rewards.id")
    )

    claimed = Column(
        Boolean,
        default=True
    )