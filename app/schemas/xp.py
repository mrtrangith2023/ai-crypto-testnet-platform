from pydantic import BaseModel


class XPResponse(BaseModel):
    user_id: int
    xp: int


class RankResponse(BaseModel):
    user_id: int
    xp: int
    rank: int