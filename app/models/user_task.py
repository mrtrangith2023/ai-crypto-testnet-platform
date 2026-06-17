from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from app.database.database import Base


class UserTask(Base):
    __tablename__ = "user_tasks"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    task_id = Column(
        Integer,
        ForeignKey("campaign_tasks.id")
    )