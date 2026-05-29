from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

users = []

@router.get("/users/")
def get_users():
    return users


@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):

    # Check duplicate email
    for existing_user in users:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    # Check duplicate username
    for existing_user in users:
        if existing_user["username"] == user.username:
            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )

    new_user = {
        "id": len(users) + 1,
        "username": user.username,
        "email": user.email
    }

    users.append(new_user)

    return new_user