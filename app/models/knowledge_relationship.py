from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.db import Base


class KnowledgeRelationship(Base):

    __tablename__ = "knowledge_relationships"

    id = Column(
        Integer,
        primary_key=True
    )

    relationship_id = Column(
        String,
        unique=True
    )

    source = Column(
        String
    )

    target = Column(
        String
    )

    relation = Column(
        String
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )