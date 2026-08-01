from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey
)

from datetime import datetime

from app.database.db import Base



class CertificationPlan(Base):


    __tablename__ = "certification_plans"



    id = Column(

        Integer,

        primary_key=True

    )


    user_id = Column(

        Integer,

        ForeignKey(
            "user_profiles.id"
        ),

        nullable=False

    )


    career = Column(

        Text,

        nullable=False

    )


    certification_content = Column(

        Text,

        nullable=False

    )


    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )