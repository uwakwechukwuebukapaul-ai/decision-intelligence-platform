from datetime import datetime
import uuid


class IntelLogger:


    def log(self,event):

        return {

            "log_id":

                "INTELLOG-" + str(uuid.uuid4())[:8],

            "event":

                "Threat intelligence analysis executed",

            "data":

                event,

            "timestamp":

                datetime.utcnow().isoformat()

        }