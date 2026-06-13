from pydantic import BaseModel


class PortfolioCreate(BaseModel):
    name: str


class PortfolioResponse(BaseModel):
    id: int
    name: str
    user_id: int

    class Config:
        from_attributes = True