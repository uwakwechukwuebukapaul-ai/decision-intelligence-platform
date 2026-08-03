from datetime import datetime
import uuid


class InvestigationTracker:


    def __init__(self):

        self.investigations=[]



    def create(self, intelligence):


        investigation={

            "investigation_id":
                f"HUNT-{uuid.uuid4().hex[:8].upper()}",

            "status":
                "ACTIVE",

            "target":
                intelligence,

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.investigations.append(
            investigation
        )


        return investigation