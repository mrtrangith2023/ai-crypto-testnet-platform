from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.auth.dependencies import (
    get_current_user
)
from app.schemas.reward import (
    RewardCreate,
    RewardResponse
)

from app.schemas.user_reward import (
    UserRewardResponse
)
from app.services.reward_service import (
    create_reward,
    claim_reward,
    get_my_rewards
)

router = APIRouter(
    prefix="/rewards",
    tags=["Rewards"]
)

@router.post(
    "/campaigns/{campaign_id}"
)
def create_campaign_reward(
    campaign_id: int,
    payload: RewardCreate,
    db: Session = Depends(get_db)
):

    return create_reward(
        db,
        campaign_id,
        payload.name,
        payload.xp
    )

@router.post(
    "/{reward_id}/claim"
)
def claim(
    reward_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return claim_reward(
        db,
        int(current_user["sub"]),
        reward_id
    )

@router.get(
    "/my"
)
def my_rewards(
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return get_my_rewards(
        db,
        int(current_user["sub"])
    )