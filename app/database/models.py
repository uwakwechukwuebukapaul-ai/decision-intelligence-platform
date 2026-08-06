"""
Sentinel DNA ORM Models

Investigation persistence models.
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




class Incident(Base):

    __tablename__ = "incidents"


    incident_id = Column(
        String,
        primary_key=True
    )


    indicator = Column(
        String,
        nullable=False
    )


    severity = Column(
        String,
        default="medium"
    )


    status = Column(
        String,
        default="open"
    )


    assigned_to = Column(
        String,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    updated_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    timeline = relationship(
        "TimelineEvent",
        back_populates="incident"
    )





class Case(Base):

    __tablename__ = "cases"


    case_id = Column(
        String,
        primary_key=True
    )


    indicator = Column(
        String,
        nullable=False
    )


    severity = Column(
        String,
        default="medium"
    )


    status = Column(
        String,
        default="open"
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )





class Evidence(Base):

    __tablename__ = "evidence"


    id = Column(
        String,
        primary_key=True
    )


    case_id = Column(
        String,
        ForeignKey(
            "cases.case_id"
        )
    )


    evidence_type = Column(
        String
    )


    data = Column(
        Text
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )





class TimelineEvent(Base):

    __tablename__ = "timeline_events"


    event_id = Column(
        String,
        primary_key=True
    )


    incident_id = Column(
        String,
        ForeignKey(
            "incidents.incident_id"
        )
    )


    stage = Column(
        String
    )


    message = Column(
        String
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    incident = relationship(
        "Incident",
        back_populates="timeline"
    )