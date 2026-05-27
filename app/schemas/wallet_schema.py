from pydantic import BaseModel

class WalletCreate(BaseModel):
    address: str
    chain: str

class UserCreate(BaseModel):
    id: int
    username: str
    email: str