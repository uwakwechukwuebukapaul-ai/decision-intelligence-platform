from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database.db import Base


class UserProfile(Base):

    __tablename__ = "user_profiles"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    # Authentication fields

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


    # Profile fields

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