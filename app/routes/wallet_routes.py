from fastapi import APIRouter
from app.schemas.wallet_schema import WalletCreate

router = APIRouter()

wallets = []

@router.get("/wallets/")
def get_wallets():
    return wallets

@router.post("/wallets/")
def create_wallet(wallet: WalletCreate):
    wallets.append(wallet.dict())
    return wallet