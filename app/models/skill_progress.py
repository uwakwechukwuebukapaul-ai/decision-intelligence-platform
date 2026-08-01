from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

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

        ForeignKey(
            "user_profiles.id"
        ),

        nullable=False

    )


    skill_name = Column(

        String(100),

        nullable=False

    )


    level = Column(

        String(50),

        default="Beginner"

    )


    progress = Column(

        Integer,

        default=0

    )


    status = Column(

        String(50),

        default="Learning"

    )


    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )


    completed_at = Column(

        DateTime,

        nullable=True

    )