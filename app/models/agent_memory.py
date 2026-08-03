from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime
)

from app.database.db import Base


class AgentMemory(Base):

    __tablename__ = "agent_memories"


    id = Column(
        Integer,
        primary_key=True
    )


    agent_id = Column(
        String,
        nullable=False
    )


    mission_id = Column(
        String,
        nullable=True
    )


    memory_type = Column(
        String,
        default="experience"
    )


    content = Column(
        Text,
        nullable=False
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )