from datetime import datetime
from app.database.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text


class AgentMessage(Base):

    __tablename__ = "agent_messages"


    id = Column(
        Integer,
        primary_key=True
    )


    message_id = Column(
        String(50),
        unique=True,
        nullable=False
    )


    sender = Column(
        String(100),
        nullable=False
    )


    receiver = Column(
        String(100),
        nullable=False
    )


    content = Column(
        Text,
        nullable=False
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )