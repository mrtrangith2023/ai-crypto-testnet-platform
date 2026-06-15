from pydantic import BaseModel


class CampaignTaskCreate(BaseModel):
    task_name: str


class CampaignTaskResponse(BaseModel):
    id: int
    campaign_id: int
    task_name: str
    status: str

    class Config:
        from_attributes = True