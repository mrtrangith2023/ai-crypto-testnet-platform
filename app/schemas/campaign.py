from pydantic import BaseModel


class CampaignCreate(BaseModel):
    name: str
    project_name: str
    status: str


class CampaignResponse(BaseModel):
    id: int
    name: str
    project_name: str
    status: str

    class Config:
        from_attributes = True