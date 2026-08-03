from datetime import datetime
from app.database.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text


class Team(Base):

    __tablename__ = "teams"


    id = Column(
        Integer,
        primary_key=True
    )


    team_id = Column(
        String(50),
        unique=True,
        nullable=False
    )


    name = Column(
        String(200),
        nullable=False
    )


    mission_id = Column(
        String(100),
        nullable=False
    )


    agents = Column(
        Text,
        nullable=False
    )


    status = Column(
        String(50),
        default="active"
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )