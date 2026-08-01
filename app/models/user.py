from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime
)

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database.db import Base



class UserProfile(Base):

    __tablename__ = "user_profiles"



    id = Column(

        Integer,

        primary_key=True,

        index=True

    )



    # ==========================
    # Authentication Fields
    # ==========================


    email = Column(

        String(150),

        unique=True,

        nullable=False,

        index=True

    )



    password_hash = Column(

        String(255),

        nullable=False

    )



    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )



    # ==========================
    # User Intelligence Profile
    # ==========================


    name = Column(

        String(100),

        nullable=False

    )



    education = Column(

        Text

    )



    experience = Column(

        Text

    )



    skills = Column(

        Text

    )



    goals = Column(

        Text

    )



    constraints = Column(

        Text

    )





    # ==========================
    # AI Intelligence Relations
    # ==========================


    reports = relationship(

        "AIReport",

        back_populates="user",

        cascade="all, delete-orphan"

    )



    skills_progress = relationship(

        "SkillProgress",

        back_populates="user",

        cascade="all, delete-orphan"

    )



    # ==========================
    # Adaptive Learning Engine
    # ==========================


    learning_progress = relationship(

        "LearningProgress",

        back_populates="user",

        cascade="all, delete-orphan"

    )