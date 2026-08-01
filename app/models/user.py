from sqlalchemy import Column, Integer, String, Text

from app.database.db import Base


class UserProfile(Base):

    __tablename__ = "user_profiles"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String(100)
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