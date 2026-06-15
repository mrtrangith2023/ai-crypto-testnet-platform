from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.campaign import (
    CampaignCreate,
    CampaignResponse
)

from app.schemas.campaign_task import (
    CampaignTaskCreate,
    CampaignTaskResponse
)

from app.services.campaign_service import (
    create_campaign,
    get_campaigns
)

from app.services.campaign_task_service import (
    create_task,
    get_tasks
)

router = APIRouter(
    prefix="/campaigns",
    tags=["Campaigns"]
)

@router.post(
    "/",
    response_model=CampaignResponse
)
def create_new_campaign(
    payload: CampaignCreate,
    db: Session = Depends(get_db)
):
    return create_campaign(
        db,
        payload
    )


@router.get(
    "/",
    response_model=list[CampaignResponse]
)
def list_campaigns(
    db: Session = Depends(get_db)
):
    return get_campaigns(db)

@router.post(
    "/{campaign_id}/tasks",
    response_model=CampaignTaskResponse
)
def add_task(
    campaign_id: int,
    payload: CampaignTaskCreate,
    db: Session = Depends(get_db)
):

    return create_task(
        db,
        campaign_id,
        payload.task_name
    )


@router.get(
    "/{campaign_id}/tasks",
    response_model=list[CampaignTaskResponse]
)
def list_tasks(
    campaign_id: int,
    db: Session = Depends(get_db)
):

    return get_tasks(
        db,
        campaign_id
    )