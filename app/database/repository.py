"""
Sentinel DNA Repository Layer

Database access abstraction.
"""


from datetime import datetime


from .db import Database





class Repository:


    def __init__(self):

        self.db = Database()



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

            VALUES (?, ?, ?, ?, ?, ?, ?)

            """,

            (

                incident["incident_id"],

                incident.get(
                    "indicator"
                ),

                incident.get(
                    "severity",
                    "medium"
                ),

                incident.get(
                    "status",
                    "open"
                ),

                incident.get(
                    "assigned_to"
                ),

                incident.get(
                    "created_at",
                    now
                ),

                now,

            )

        )


        return incident




    def get_incident(
        self,
        incident_id,
    ):


        result = self.db.execute_one(

            """

            SELECT *

            FROM incidents

            WHERE incident_id = ?

            """,

            (
                incident_id,
            )

        )


        return dict(result) if result else None




    def list_incidents(self):


        rows = self.db.execute(

            """

            SELECT *

            FROM incidents

            ORDER BY id DESC

            """

        )


        return [

            dict(row)

            for row in rows

        ]