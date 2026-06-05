# from fastapi import APIRouter

# router = APIRouter(
#     prefix="/wallets",
#     tags=["Wallets"]
# )

# @router.get("/")
# def get_wallets():
#     return {
#         "wallets": [],
#         "message": "Wallet list endpoint"
#     }

# @router.post("/")
# def create_wallet():
#     return {
#         "message": "Create wallet endpoint"
#     }
from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.auth.dependencies import (
    get_current_user
)

from app.schemas.wallet import (
    WalletCreate,
    WalletResponse
)

from app.services.wallet_service import (
    create_wallet,
    get_wallets
)

router = APIRouter(
    prefix="/wallets",
    tags=["Wallets"]
)

@router.post(
    "/",
    response_model=WalletResponse
)
def create_new_wallet(
    payload: WalletCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return create_wallet(
        db,
        payload,
        int(current_user["sub"])
    )

@router.get(
    "/",
    response_model=list[WalletResponse]
)
def get_my_wallets(
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return get_wallets(
        db,
        int(current_user["sub"])
    )