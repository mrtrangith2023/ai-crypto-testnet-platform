from app.database.database import engine, Base

from app.models.wallet import Wallet
from app.models.user import User

def init_db():
    Base.metadata.create_all(bind=engine)