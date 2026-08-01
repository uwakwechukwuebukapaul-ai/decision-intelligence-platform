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



    week = Column(

        Integer,

        nullable=False

    )



    title = Column(

        String(200),

        nullable=False

    )



    description = Column(

        Text,

        nullable=False

    )



    status = Column(

        String(50),

        default="Pending"

    )



    completed_at = Column(

        DateTime,

        nullable=True

    )



    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )



    user = relationship(

        "UserProfile",

        back_populates="learning_progress"

    )