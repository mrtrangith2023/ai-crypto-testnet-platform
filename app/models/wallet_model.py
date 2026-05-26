from sqlalchemy import Column, Integer, String

from app.database.database import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, unique=True, index=True)
    chain = Column(String)