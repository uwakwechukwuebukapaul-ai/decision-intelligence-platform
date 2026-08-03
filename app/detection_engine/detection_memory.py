import uuid
from datetime import datetime


class DetectionMemory:


    def store(self,event):

        return {

            "memory_id":
                "DETECT-" + str(uuid.uuid4())[:8].upper(),

            "event":
                event,

            "stored":

            [
                "Detection History",
                "Rule Execution",
                "Alert Decisions"
            ],

            "timestamp":
                datetime.utcnow().isoformat()

        }