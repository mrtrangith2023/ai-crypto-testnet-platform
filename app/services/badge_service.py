from sqlalchemy.orm import Session

from app.models.badge import Badge
from app.models.user_reward import UserReward
from app.models.reward import Reward


def create_badge(
    db: Session,
    name: str,
    xp_required: int
):

    badge = Badge(
        name=name,
        xp_required=xp_required
    )

    db.add(badge)
    db.commit()
    db.refresh(badge)

    return badge


def get_badges(db: Session):

    return db.query(
        Badge
    ).order_by(
        Badge.xp_required
    ).all()


def get_my_badge(
    db: Session,
    user_id: int
):

    rewards = (
        db.query(
            UserReward,
            Reward
        )
        .join(
            Reward,
            UserReward.reward_id == Reward.id
        )
        .filter(
            UserReward.user_id == user_id
        )
        .all()
    )

    xp = sum(
        reward.xp
        for _, reward in rewards
    )

    badges = db.query(
        Badge
    ).order_by(
        Badge.xp_required
    ).all()

    current = "No Badge"

    for badge in badges:
        if xp >= badge.xp_required:
            current = badge.name

    return {
        "user_id": user_id,
        "xp": xp,
        "badge": current
    }