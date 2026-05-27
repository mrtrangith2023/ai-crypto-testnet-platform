from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate

def create_user(db: Session, user_data: UserCreate):
    user = User(
        username=user_data.username,
        email=user_data.email,
        password=user_data.password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_users(db: Session):
    return db.query(User).all()