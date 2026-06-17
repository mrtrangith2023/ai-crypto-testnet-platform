from pydantic import BaseModel


class UserTaskResponse(BaseModel):
    id: int
    user_id: int
    task_id: int

    class Config:
        from_attributes = True