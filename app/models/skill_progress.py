from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.db import Base



class SkillProgress(Base):

    __tablename__ = "skill_progress"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    skill_name = Column(
        String,
        nullable=False
    )


    level = Column(
        String,
        default="Beginner"
    )


    progress = Column(
        Integer,
        default=0
    )


    status = Column(
        String,
        default="Learning"
    )


    started_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    completed_at = Column(
        DateTime,
        nullable=True
    )


    user = relationship(
        "UserProfile",
        back_populates="skills_progress"
    )