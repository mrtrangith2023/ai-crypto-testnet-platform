from pydantic import BaseModel


class ProjectNoteCreate(BaseModel):
    note: str


class ProjectNoteResponse(BaseModel):
    id: int
    user_id: int
    project_id: int
    note: str

    class Config:
        from_attributes = True