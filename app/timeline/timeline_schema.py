"""
Sentinel DNA Timeline Schema
"""


from dataclasses import dataclass
from datetime import datetime



@dataclass
class TimelineEvent:

    event_id: str

    incident_id: str

    stage: str

    message: str

    created_at: str = (
        datetime.utcnow().isoformat()
    )


    def to_dict(self):

        return {

            "event_id": self.event_id,

            "incident_id": self.incident_id,

            "stage": self.stage,

            "message": self.message,

            "created_at": self.created_at,

        }