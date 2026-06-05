from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.database.database import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(
        Integer,
        primary_key=True
    )

    address = Column(
        String,
        unique=True,
        index=True
    )

    chain = Column(String)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    owner = relationship(
        "User",
        back_populates="wallets"
    )

from app.models.user import User