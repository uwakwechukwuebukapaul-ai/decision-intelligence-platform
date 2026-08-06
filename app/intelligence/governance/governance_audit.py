"""
Decision Intelligence Platform

Governance Audit Service

Persistent-ready audit foundation for
intelligence governance decisions.

Responsibilities:
- Governance decision history
- Execution audit trail
- Compliance evidence
- Security review support
- Enterprise observability foundation
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import List, Dict
from threading import RLock



# =====================================
# Audit Event Model
# =====================================

@dataclass
class GovernanceAuditEvent:

    capability: str

    action: str

    decision: str

    user_id: str | None = None

    objective: str | None = None

    reason: str | None = None

    metadata: dict = field(
        default_factory=dict
    )

    timestamp: str = field(
        default_factory=lambda:
        datetime.now(UTC).isoformat()
    )


    def to_dict(self):

        return {

            "capability":
                self.capability,

            "action":
                self.action,

            "decision":
                self.decision,

            "user_id":
                self.user_id,

            "objective":
                self.objective,

            "reason":
                self.reason,

            "metadata":
                self.metadata,

            "timestamp":
                self.timestamp

        }



# =====================================
# Governance Audit Manager
# =====================================

class GovernanceAuditManager:


    """
    Central governance audit collector.

    Future persistence targets:
    - SQLite
    - PostgreSQL
    - SIEM
    - Data warehouse
    """


    def __init__(self):

        self.events: List[
            GovernanceAuditEvent
        ] = []

        self.lock = RLock()



    # =================================
    # Record Event
    # =================================

    def record(

        self,

        capability: str,

        action: str,

        decision: str,

        user_id: str | None = None,

        objective: str | None = None,

        reason: str | None = None,

        metadata: dict | None = None

    ):


        event = GovernanceAuditEvent(

            capability=capability,

            action=action,

            decision=decision,

            user_id=user_id,

            objective=objective,

            reason=reason,

            metadata=metadata or {}

        )


        with self.lock:

            self.events.append(
                event
            )


        return event



    # =================================
    # Query History
    # =================================

    def get_events(self):

        with self.lock:

            return [

                event.to_dict()

                for event
                in self.events

            ]



    # =================================
    # Filter By Capability
    # =================================

    def get_by_capability(

        self,

        capability: str

    ):


        with self.lock:

            return [

                event.to_dict()

                for event
                in self.events

                if event.capability ==
                capability

            ]



    # =================================
    # Filter By Decision
    # =================================

    def get_by_decision(

        self,

        decision: str

    ):


        with self.lock:

            return [

                event.to_dict()

                for event
                in self.events

                if event.decision ==
                decision

            ]



    # =================================
    # Statistics
    # =================================

    def statistics(self):

        with self.lock:

            total = len(
                self.events
            )

            allowed = len(

                [

                    event

                    for event
                    in self.events

                    if event.decision ==
                    "allowed"

                ]

            )

            blocked = len(

                [

                    event

                    for event
                    in self.events

                    if event.decision ==
                    "blocked"

                ]

            )


        return {

            "total_events":
                total,

            "allowed":
                allowed,

            "blocked":
                blocked

        }



# =====================================
# Global Audit Service
# =====================================

governance_audit = (
    GovernanceAuditManager()
)