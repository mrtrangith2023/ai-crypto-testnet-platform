from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.database import Base

class Project(Base):

    __tablename__ = "projects"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
        unique=True
    )

    ecosystem = Column(String)

    funding = Column(String)

    status = Column(String)

    website = Column(String)

    twitter = Column(String)