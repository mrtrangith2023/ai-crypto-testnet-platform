from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.database import Base


class CampaignTask(Base):
    __tablename__ = "campaign_tasks"

    id = Column(
        Integer,
        primary_key=True
    )

    campaign_id = Column(
        Integer,
        ForeignKey("campaigns.id")
    )

    task_name = Column(
        String
    )

    status = Column(
        String,
        default="pending"
    )