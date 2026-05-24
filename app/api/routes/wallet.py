from fastapi import APIRouter

router = APIRouter(
    prefix="/wallets",
    tags=["Wallets"]
)

@router.get("/")
def get_wallets():
    return {
        "wallets": [],
        "message": "Wallet list endpoint"
    }

@router.post("/")
def create_wallet():
    return {
        "message": "Create wallet endpoint"
    }