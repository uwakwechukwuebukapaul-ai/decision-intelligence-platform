from datetime import datetime
from app.database.db import Base
from sqlalchemy import Column, Integer, String, Text, DateTime


class MissionResult(Base):

    __tablename__ = "mission_results"


    id = Column(
        Integer,
        primary_key=True
    )


    mission_id = Column(
        String,
        nullable=False
    )


    agent_id = Column(
        String,
        nullable=False
    )


    result = Column(
        Text,
        nullable=False
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )