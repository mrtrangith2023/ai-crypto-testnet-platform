from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

class UserCreate(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=20,
        description="Unique username"
    )

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=50
    )

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True