from sqlalchemy.orm import Session

from app.models.user_task import UserTask
from app.models.campaign_task import (
    CampaignTask
)

def complete_task(
    db: Session,
    user_id: int,
    task_id: int
):

    record = UserTask(
        user_id=user_id,
        task_id=task_id
    )

    db.add(record)

    db.commit()

    db.refresh(record)

    return record

def get_campaign_progress(
    db: Session,
    campaign_id: int,
    user_id: int
):

    tasks = db.query(
        CampaignTask
    ).filter(
        CampaignTask.campaign_id == campaign_id
    ).all()

    total = len(tasks)

    task_ids = [
        t.id
        for t in tasks
    ]

    completed = db.query(
        UserTask
    ).filter(
        UserTask.user_id == user_id,
        UserTask.task_id.in_(task_ids)
    ).count()

    progress = 0

    if total > 0:
        progress = round(
            completed / total * 100
        )

    return {
        "campaign_id": campaign_id,
        "completed": completed,
        "total": total,
        "progress": progress
    }