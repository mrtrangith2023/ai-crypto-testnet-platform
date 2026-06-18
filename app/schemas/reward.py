from pydantic import BaseModel


class RewardCreate(BaseModel):
    name: str
    xp: int


class RewardResponse(BaseModel):
    id: int
    campaign_id: int
    name: str
    xp: int

    class Config:
        from_attributes = True