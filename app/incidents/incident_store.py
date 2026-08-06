"""
Sentinel DNA - Incident Store

Storage abstraction layer.
"""


from __future__ import annotations





class IncidentStore:
    """
    Temporary incident repository.

    Designed for future:
    - SQLite
    - PostgreSQL
    - distributed storage
    """



    def __init__(self):

        self.incidents = {}



    def save(
        self,
        incident: dict,
    ) -> dict:

        self.incidents[
            incident["incident_id"]
        ] = incident


        return incident



    def get(
        self,
        incident_id: str,
    ) -> dict | None:

        return self.incidents.get(
            incident_id
        )



    def all(
        self,
    ) -> list:

        return list(
            self.incidents.values()
        )