from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.user import User

from app.auth.security import (
    verify_password,
    create_access_token
)

def login_user(
    email: str,
    password: str,
    db: Session
):
    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }