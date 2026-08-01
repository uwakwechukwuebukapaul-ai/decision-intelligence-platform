from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database.db import Base



class LearningProgress(Base):

    __tablename__ = "learning_progress"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        ForeignKey(
            "user_profiles.id"
        ),
        nullable=False
    )


    skill_name = Column(
        String(100),
        nullable=False
    )


    progress = Column(
        Integer,
        default=0
    )


    status = Column(
        String(50),
        default="Not Started"
    )


    notes = Column(
        Text
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    user = relationship(
        "UserProfile",
        back_populates="learning_progress"
    )