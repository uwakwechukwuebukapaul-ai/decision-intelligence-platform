"""
Sentinel DNA Database Models

SQLAlchemy ORM models.
"""


from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
)

from .db import Base





class Incident(Base):

    __tablename__ = " incidents".strip()


    incident_id = Column(
        String,
        primary_key=True,
    )


    indicator = Column(
        String,
        nullable=False,
    )


    severity = Column(
        String,
        default="medium",
    )


    status = Column(
        String,
        default="open",
    )


    assigned_to = Column(
        String,
        nullable=True,
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )


    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )





class Case(Base):

    __tablename__ = "cases"


    case_id = Column(
        String,
        primary_key=True,
    )


    indicator = Column(
        String,
        nullable=False,
    )


    severity = Column(
        String,
        default="medium",
    )


    status = Column(
        String,
        default="open",
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )





class Evidence(Base):

    __tablename__ = "evidence"


    id = Column(
        String,
        primary_key=True,
    )


    case_id = Column(
        String,
        nullable=False,
    )


    evidence_type = Column(
        String,
    )


    data = Column(
        Text,
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )