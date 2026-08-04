from datetime import datetime
import uuid


class InvestigationController:


    def start(self,event):

        return {

            "investigation_id":
                "INV-" + uuid.uuid4().hex[:8].upper(),

            "event":event,

            "status":"investigation_started",

            "timestamp":
                datetime.utcnow().isoformat()

        }