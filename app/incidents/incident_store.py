"""
Sentinel DNA - Incident Store

Persistent incident storage adapter.
"""

from __future__ import annotations

from datetime import datetime

from app.database import Repository


class IncidentStore:
    """
    Persistent incident repository.

    Uses Sentinel DNA database layer.
    """

    def __init__(self):
        self.repository = Repository()


    def save(
        self,
        incident: dict,
    ) -> dict:

        incident["updated_at"] = (
            datetime.utcnow().isoformat()
        )

        self.repository.save_incident(
            incident
        )

        return incident



    def get(
        self,
        incident_id: str,
    ) -> dict | None:

        return self.repository.get_incident(
            incident_id
        )



    def all(
        self,
    ) -> list:

        return self.repository.list_incidents()