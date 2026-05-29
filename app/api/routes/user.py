from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.user import UserCreate
from app.schemas.user import UserResponse

from app.services.user_service import create_user
from app.services.user_service import get_users

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)

@router.get(
    "/",
    response_model=list[UserResponse],
    status_code=status.HTTP_200_OK
)
def get_all_users(
    db: Session = Depends(get_db)
):
    return get_users(db)