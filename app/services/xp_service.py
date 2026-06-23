from sqlalchemy.orm import Session

from app.models.user_reward import UserReward
from app.models.reward import Reward

def get_user_xp(
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

    total_xp = sum(
        reward.xp
        for _, reward in rewards
    )

    return {
        "user_id": user_id,
        "xp": total_xp
    }

def get_leaderboard(
    db: Session
):

    users = {}

    rewards = (
        db.query(
            UserReward,
            Reward
        )
        .join(
            Reward,
            UserReward.reward_id == Reward.id
        )
        .all()
    )

    for user_reward, reward in rewards:

        if user_reward.user_id not in users:

            users[user_reward.user_id] = 0

        users[user_reward.user_id] += reward.xp

    leaderboard = []

    for user_id, xp in users.items():

        leaderboard.append(
            {
                "user_id": user_id,
                "xp": xp
            }
        )

    leaderboard.sort(
        key=lambda x: x["xp"],
        reverse=True
    )

    return leaderboard

def get_user_rank(
    db: Session,
    user_id: int
):

    leaderboard = get_leaderboard(db)

    for index, user in enumerate(
        leaderboard,
        start=1
    ):

        if user["user_id"] == user_id:

            return {
                "user_id": user_id,
                "xp": user["xp"],
                "rank": index
            }

    return {
        "user_id": user_id,
        "xp": 0,
        "rank": 0
    }