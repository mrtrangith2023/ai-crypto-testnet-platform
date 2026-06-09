from pydantic import BaseModel

class ProjectCreate(BaseModel):

    name: str

    ecosystem: str

    funding: str

    status: str

    website: str

    twitter: str

class ProjectResponse(BaseModel):

    id: int

    name: str

    ecosystem: str

    funding: str

    status: str

    website: str

    twitter: str

    class Config:
        from_attributes = True