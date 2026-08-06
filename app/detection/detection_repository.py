from datetime import datetime

from app.database import Database



class DetectionRepository:


    def __init__(self):

        self.db = Database()



    def save(
        self,
        detection: dict
    ):


        self.db.execute(

            """
            INSERT INTO detections

            (
                detection_id,
                incident_id,
                rule,
                severity,
                indicator,
                status,
                created_at
            )

            VALUES

            (
                :detection_id,
                :incident_id,
                :rule,
                :severity,
                :indicator,
                :status,
                :created_at
            )

            """,

            detection

        )


        return detection