from sqlalchemy.orm import Session

from app.models.campaign import Campaign


def create_campaign(
    db: Session,
    payload
):

    campaign = Campaign(
        name=payload.name,
        project_name=payload.project_name,
        status=payload.status
    )

    db.add(campaign)

    db.commit()

    db.refresh(campaign)

    return campaign


def get_campaigns(
    db: Session
):

    return db.query(
        Campaign
    ).all()