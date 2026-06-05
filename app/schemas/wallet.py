from pydantic import BaseModel
from pydantic import Field
from pydantic import BaseModel
from pydantic import Field

class WalletCreate(BaseModel):
    address: str = Field(
        min_length=42,
        max_length=42
    )

    chain: str = Field(
        min_length=2,
        max_length=30
    )

class WalletResponse(BaseModel):
    id: int
    address: str
    chain: str
    user_id: int

    class Config:
        from_attributes = True