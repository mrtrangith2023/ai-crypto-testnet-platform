from sqlalchemy.orm import Session

from app.models.campaign_task import (
    CampaignTask
)


def create_task(
    db: Session,
    campaign_id: int,
    task_name: str
):

    task = CampaignTask(
        campaign_id=campaign_id,
        task_name=task_name
    )

    db.add(task)

    db.commit()

    db.refresh(task)

    return task


def get_tasks(
    db: Session,
    campaign_id: int
):

    return db.query(
        CampaignTask
    ).filter(
        CampaignTask.campaign_id == campaign_id
    ).all()