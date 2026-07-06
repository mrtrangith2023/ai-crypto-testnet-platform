from pydantic import BaseModel


class BadgeCreate(BaseModel):
    name: str
    xp_required: int


class BadgeResponse(BadgeCreate):
    id: int

    class Config:
        from_attributes = True


class MyBadgeResponse(BaseModel):
    user_id: int
    xp: int
    badge: str