from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database.db import Base


class KnowledgeNode(Base):

    __tablename__ = "knowledge_nodes"

    id = Column(
        Integer,
        primary_key=True
    )

    node_id = Column(
        String,
        unique=True
    )

    node_type = Column(
        String
    )

    name = Column(
        String
    )

    data = Column(
        Text
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )