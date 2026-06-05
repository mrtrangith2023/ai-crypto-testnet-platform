from app.database.database import engine, Base

from app.models.user import User
from app.models.wallet import Wallet

def init_db():
    Base.metadata.create_all(bind=engine)