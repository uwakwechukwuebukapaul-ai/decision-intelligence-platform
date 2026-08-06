"""
Sentinel DNA - Incident Manager

SOC incident lifecycle controller.

Responsibilities:

- Create incidents
- Update incident state
- Assign analysts
- Add investigation notes
- Retrieve incidents
"""


from __future__ import annotations


from datetime import datetime


from .incident_status import IncidentStatus
from .incident_store import IncidentStore





class IncidentManager:
    """
    Controls incident lifecycle operations.
    """



    def __init__(self):

        self.store = IncidentStore()



    def create_incident(
        self,
        incident: dict,
    ) -> dict:
        """
        Register a new SOC incident.
        """

        incident["status"] = (
            IncidentStatus.OPEN.value
        )


        incident["created_at"] = (
            datetime.utcnow().isoformat()
        )


        incident["updated_at"] = (
            datetime.utcnow().isoformat()
        )


        incident["notes"] = []

        incident["assigned_to"] = None


        return self.store.save(
            incident
        )



    def update_status(
        self,
        incident_id: str,
        status: IncidentStatus,
    ) -> dict | None:
        """
        Move incident through lifecycle.
        """

        incident = self.store.get(
            incident_id
        )


        if not incident:

            return None



        incident["status"] = status.value

        incident["updated_at"] = (
            datetime.utcnow().isoformat()
        )


        return self.store.save(
            incident
        )



    def assign_analyst(
        self,
        incident_id: str,
        analyst: str,
    ) -> dict | None:
        """
        Assign SOC analyst ownership.
        """

        incident = self.store.get(
            incident_id
        )


        if not incident:

            return None



        incident["assigned_to"] = analyst


        incident["updated_at"] = (
            datetime.utcnow().isoformat()
        )


        return self.store.save(
            incident
        )



    def add_note(
        self,
        incident_id: str,
        note: str,
    ) -> dict | None:
        """
        Add analyst investigation note.
        """

        incident = self.store.get(
            incident_id
        )


        if not incident:

            return None



        incident["notes"].append(

            {
                "note": note,

                "timestamp":
                    datetime.utcnow().isoformat(),

            }

        )


        incident["updated_at"] = (
            datetime.utcnow().isoformat()
        )


        return self.store.save(
            incident
        )



    def get_incident(
        self,
        incident_id: str,
    ) -> dict | None:

        return self.store.get(
            incident_id
        )



    def list_incidents(
        self,
    ) -> list:

        return self.store.all()