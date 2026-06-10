from pydantic import BaseModel

class WatchlistCreate(BaseModel):

    project_id: int

class WatchlistResponse(BaseModel):

    id: int

    user_id: int

    project_id: int

    class Config:
        from_attributes = True