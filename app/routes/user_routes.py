from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserResponse
from sqlalchemy.orm import Session
from fastapi import Depends

from app.models.user import User
from app.database.dependencies import get_db
from app.auth.security import hash_password

router = APIRouter()

@router.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/users/")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    # Check duplicate email
    existing_email = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Check duplicate username
    existing_username = (
        db.query(User)
        .filter(User.username == user.username)
        .first()
    )

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    hashed_password = hash_password(
        user.password
    )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user