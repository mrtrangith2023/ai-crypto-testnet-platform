from pydantic import BaseModel


class CampaignProgressResponse(BaseModel):
    campaign_id: int
    completed: int
    total: int
    progress: int