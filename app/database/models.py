"""
Sentinel DNA Database Models

SQLAlchemy ORM models.

Enterprise investigation persistence layer.
"""


from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from .db import Base





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


    incidents = relationship(
        "Incident",
        back_populates="case",
    )


    evidence = relationship(
        "Evidence",
        back_populates="case",
    )


    timeline = relationship(
        "TimelineEvent",
        back_populates="case",
    )





class Incident(Base):

    __tablename__ = "incidents"


    incident_id = Column(
        String,
        primary_key=True,
    )


    case_id = Column(
        String,
        ForeignKey(
            "cases.case_id"
        ),
        nullable=False,
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


    case = relationship(
        "Case",
        back_populates="incidents",
    )





class Evidence(Base):

    __tablename__ = "evidence"


    evidence_id = Column(
        String,
        primary_key=True,
    )


    case_id = Column(
        String,
        ForeignKey(
            "cases.case_id"
        ),
        nullable=False,
    )


    evidence_type = Column(
        String,
        nullable=False,
    )


    data = Column(
        Text,
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )


    case = relationship(
        "Case",
        back_populates="evidence",
    )





class TimelineEvent(Base):

    __tablename__ = "timeline_events"


    id = Column(
        String,
        primary_key=True,
    )


    case_id = Column(
        String,
        ForeignKey(
            "cases.case_id"
        ),
        nullable=False,
    )


    stage = Column(
        String,
        nullable=False,
    )


    message = Column(
        Text,
        nullable=False,
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )


    case = relationship(
        "Case",
        back_populates="timeline",
    )