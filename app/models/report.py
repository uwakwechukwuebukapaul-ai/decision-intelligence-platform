from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database.db import Base



class AIReport(Base):


    __tablename__ = "ai_reports"



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



    report_content = Column(

        Text,

        nullable=False

    )



    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )



    # ==========================
    # Relationship
    # ==========================


    user = relationship(

        "UserProfile",

        back_populates="reports"

    )