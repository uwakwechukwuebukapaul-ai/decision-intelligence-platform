from datetime import datetime
from app.database.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text


class ConsensusResult(Base):

    __tablename__ = "consensus_results"


    id = Column(
        Integer,
        primary_key=True
    )


    consensus_id = Column(
        String(50),
        unique=True,
        nullable=False
    )


    mission_id = Column(
        String(100),
        nullable=False
    )


    recommendation = Column(
        Text,
        nullable=False
    )


    confidence = Column(
        Integer,
        default=0
    )


    status = Column(
        String(50),
        default="completed"
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )