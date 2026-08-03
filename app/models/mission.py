from datetime import datetime
from app.database.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text


class Mission(Base):

    __tablename__ = "missions"


    id = Column(
        Integer,
        primary_key=True
    )


    mission_id = Column(
        String,
        unique=True,
        nullable=False
    )


    title = Column(
        String,
        nullable=False
    )


    objective = Column(
        Text,
        nullable=False
    )


    priority = Column(
        String,
        default="medium"
    )


    status = Column(
        String,
        default="created"
    )


    assigned_agent = Column(
        String,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    completed_at = Column(
        DateTime,
        nullable=True
    )