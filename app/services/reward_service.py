from sqlalchemy.orm import Session

from app.models.reward import Reward
from app.models.user_reward import UserReward

from app.models.campaign import Campaign

from fastapi import HTTPException

def create_reward(
    db: Session,
    campaign_id: int,
    name: str,
    xp: int
):

    campaign = db.query(
        Campaign
    ).filter(
        Campaign.id == campaign_id
    ).first()

    if not campaign:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    reward = Reward(
        campaign_id=campaign_id,
        name=name,
        xp=xp
    )

    db.add(reward)

    db.commit()

    db.refresh(reward)

    return reward

def claim_reward(
    db: Session,
    user_id: int,
    reward_id: int
):

    reward = db.query(
        Reward
    ).filter(
        Reward.id == reward_id
    ).first()

    if not reward:
        raise HTTPException(
            status_code=404,
            detail="Reward not found"
        )

    claim = UserReward(
        user_id=user_id,
        reward_id=reward_id
    )

    db.add(claim)

    db.commit()

    db.refresh(claim)

    return claim

def get_my_rewards(
    db: Session,
    user_id: int
):

    return db.query(
        UserReward
    ).filter(
        UserReward.user_id == user_id
    ).all()