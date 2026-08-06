"""
Sentinel DNA - Analyst Workspace Engine

Provides SOC analyst operations.
"""


from __future__ import annotations


from .workspace_schema import WorkspaceIncident
from .workspace_store import WorkspaceStore





class AnalystWorkspace:


    def __init__(self):

        self.store = WorkspaceStore()



    def create_workspace_incident(
        self,
        incident: dict,
    ):


        workspace_incident = WorkspaceIncident(

            incident_id=
            incident.get(
                "incident_id"
            ),

            indicator=
            incident.get(
                "indicator",
                "unknown"
            ),

            severity=
            incident.get(
                "severity",
                "medium"
            ),

            status=
            incident.get(
                "status",
                "open"
            ),

            assigned_to=
            incident.get(
                "assigned_to"
            ),

            timeline=
            incident.get(
                "timeline",
                []
            ),

        )


        return self.store.save(
            workspace_incident.to_dict()
        )




    def get_incident_queue(self):

        return self.store.open_incidents()




    def assign_incident(
        self,
        incident_id: str,
        analyst: str,
    ):


        incident = self.store.get(
            incident_id
        )


        if not incident:

            return None



        incident["assigned_to"] = analyst


        incident["timeline"].append(

            {

                "stage":
                    "assignment",

                "message":
                    f"Assigned to {analyst}",

            }

        )


        return incident




    def update_status(
        self,
        incident_id: str,
        status: str,
    ):


        incident = self.store.get(
            incident_id
        )


        if not incident:

            return None



        incident["status"] = status


        incident["timeline"].append(

            {

                "stage":
                    "status",

                "message":
                    f"Status changed to {status}",

            }

        )


        return incident