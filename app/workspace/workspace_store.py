"""
Sentinel DNA - Workspace Store

Temporary workspace persistence layer.

Future expansion:
- PostgreSQL
- Redis cache
- Elasticsearch indexing
"""


from __future__ import annotations





class WorkspaceStore:


    def __init__(self):

        self.incidents = {}



    def save(
        self,
        incident: dict,
    ):

        self.incidents[
            incident["incident_id"]
        ] = incident


        return incident




    def get(
        self,
        incident_id: str,
    ):

        return self.incidents.get(
            incident_id
        )




    def all(self):

        return list(
            self.incidents.values()
        )




    def open_incidents(self):

        return [

            incident

            for incident in self.incidents.values()

            if incident.get(
                "status"
            ) != "closed"

        ]