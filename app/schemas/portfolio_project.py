from pydantic import BaseModel


class PortfolioProjectCreate(BaseModel):
    project_id: int


class PortfolioProjectResponse(BaseModel):
    id: int
    portfolio_id: int
    project_id: int

    class Config:
        from_attributes = True