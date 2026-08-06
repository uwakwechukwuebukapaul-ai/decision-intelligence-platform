"""
Sentinel DNA Timeline Manager
"""


from datetime import datetime
import uuid


from .timeline_repository import TimelineRepository





class TimelineManager:


    def __init__(self):

        self.repository = TimelineRepository()



    def add_event(
        self,
        incident_id,
        stage,
        message,
    ):


        event = {

            "event_id":
                f"EVT-{uuid.uuid4().hex[:8]}",

            "incident_id":
                incident_id,

            "stage":
                stage,

            "message":
                message,

            "created_at":
                datetime.utcnow().isoformat(),

        }


        return self.repository.save(
            event
        )



    def get_events(
        self,
        incident_id,
    ):

        return self.repository.get(
            incident_id
        )