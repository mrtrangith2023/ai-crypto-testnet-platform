from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(String, unique=True)

    email = Column(String, unique=True)

    password = Column(String)

    role = Column(
        String,
        default="user"
    )

    wallets = relationship(
        "Wallet",
        back_populates="owner"
    )

    portfolios = relationship(
    "Portfolio",
    back_populates="owner"
)

from app.models.wallet import Wallet