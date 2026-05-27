from fastapi import APIRouter
from app.schemas.wallet_schema import UserCreate

router = APIRouter()

users = []

@router.get("/users/")
def get_users():
    return users

@router.post("/users/")
def create_user(user: UserCreate):
    users.append(user.dict())
    return user