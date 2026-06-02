from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.auth.security import hash_password

def create_user(db: Session, user_data: UserCreate):

    existing_email = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    existing_username = db.query(User).filter(
        User.username == user_data.username
    ).first()

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    user = User(
        username=user_data.username,
        email=user_data.email,
        password=hash_password(
            user_data.password
        ),
        role="user"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_users(db: Session):
    return db.query(User).all()