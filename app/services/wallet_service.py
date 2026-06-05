from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.wallet import Wallet

from app.schemas.wallet import WalletCreate

from app.utils.validators import (
    is_valid_eth_address
)

def create_wallet(
    db: Session,
    payload: WalletCreate,
    user_id: int
):

    if not is_valid_eth_address(
        payload.address
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid wallet address"
        )

    existing = db.query(
        Wallet
    ).filter(
        Wallet.address == payload.address
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Wallet already exists"
        )

    wallet = Wallet(
        address=payload.address,
        chain=payload.chain,
        user_id=user_id
    )

    db.add(wallet)

    db.commit()

    db.refresh(wallet)

    return wallet

def get_wallets(
    db: Session,
    user_id: int
):

    return db.query(
        Wallet
    ).filter(
        Wallet.user_id == user_id
    ).all()