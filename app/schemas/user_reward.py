from pydantic import BaseModel


class UserRewardResponse(BaseModel):
    id: int
    user_id: int
    reward_id: int
    claimed: bool

    class Config:
        from_attributes = True