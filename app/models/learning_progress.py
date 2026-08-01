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


    # ==========================
    # Primary Key
    # ==========================

    id = Column(

        Integer,

        primary_key=True,

        index=True

    )



    # ==========================
    # User Relationship
    # ==========================

    user_id = Column(

        Integer,

        ForeignKey(
            "user_profiles.id"
        ),

        nullable=False

    )



    # ==========================
    # Learning Roadmap Fields
    # ==========================

    week = Column(

        Integer,

        nullable=False

    )



    skill_name = Column(

        String(100),

        nullable=False

    )



    objective = Column(

        Text

    )



    # ==========================
    # Progress Tracking
    # ==========================

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



    # ==========================
    # Completion Tracking
    # ==========================

    completed_at = Column(

        DateTime,

        nullable=True

    )



    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )



    # ==========================
    # SQLAlchemy Relationship
    # ==========================

    user = relationship(

        "UserProfile",

        back_populates="learning_progress"

    )