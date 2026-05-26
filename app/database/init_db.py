from app.database.database import engine, Base

from app.models.wallet_model import Wallet

def init_db():
    Base.metadata.create_all(bind=engine)