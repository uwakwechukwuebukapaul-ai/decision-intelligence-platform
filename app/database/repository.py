"""
Sentinel DNA Database Repository

Enterprise persistence abstraction layer.

Handles:

- Incident persistence
- Timeline persistence
- Evidence persistence
"""

from datetime import datetime

from .db import Database



class Repository:


    def __init__(self):

        self.db = Database()



    # ==========================
    # INCIDENTS
    # ==========================

    def save_incident(
        self,
        incident: dict,
    ):

        now = datetime.utcnow().isoformat()


        self.db.execute(

            """
            INSERT OR REPLACE INTO incidents

            (
                incident_id,
                indicator,
                severity,
                status,
                assigned_to,
                created_at,
                updated_at
            )

            VALUES
            (
                :incident_id,
                :indicator,
                :severity,
                :status,
                :assigned_to,
                :created_at,
                :updated_at
            )
            """,

            {

                "incident_id":
                    incident["incident_id"],

                "indicator":
                    incident.get(
                        "indicator"
                    ),

                "severity":
                    incident.get(
                        "severity",
                        "medium"
                    ),

                "status":
                    incident.get(
                        "status",
                        "open"
                    ),

                "assigned_to":
                    incident.get(
                        "assigned_to"
                    ),

                "created_at":
                    incident.get(
                        "created_at",
                        now
                    ),

                "updated_at":
                    now,

            }

        )


        return incident



    def get_incident(
        self,
        incident_id: str,
    ):


        return self.db.execute_one(

            """
            SELECT *

            FROM incidents

            WHERE incident_id = :incident_id
            """,

            {
                "incident_id":
                    incident_id
            }

        )



    def list_incidents(self):


        return self.db.execute(

            """
            SELECT *

            FROM incidents

            ORDER BY created_at DESC
            """

        )



    # ==========================
    # TIMELINE
    # ==========================


    def save_timeline_event(
        self,
        event: dict,
    ):

        self.db.execute(

            """
            INSERT INTO timeline_events

            (
                id,
                event_id,
                case_id,
                incident_id,
                stage,
                message,
                created_at
            )

            VALUES

            (
                :id,
                :event_id,
                :case_id,
                :incident_id,
                :stage,
                :message,
                :created_at
            )
            """,

            {

                "id":
                    event["event_id"],


                "event_id":
                    event["event_id"],


                "case_id":
                    event.get(
                        "case_id",
                        event.get(
                            "incident_id"
                        )
                    ),


                "incident_id":
                    event.get(
                        "incident_id"
                    ),


                "stage":
                    event["stage"],


                "message":
                    event["message"],


                "created_at":
                    event["created_at"],

            }

        )


        return event



    def get_timeline(
        self,
        incident_id: str,
    ):


        return self.db.execute(

            """
            SELECT *

            FROM timeline_events

            WHERE incident_id = :incident_id

            ORDER BY created_at ASC
            """,

            {

                "incident_id":
                    incident_id

            }

        )