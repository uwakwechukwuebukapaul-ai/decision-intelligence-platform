from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
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


    career = Column(

        String(100),

        nullable=False

    )


    week = Column(

        Integer,

        nullable=False

    )


    skill = Column(

        String(100),

        nullable=False

    )


    objective = Column(

        Text

    )


    completed = Column(

        Boolean,

        default=False

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