import uuid
from datetime import datetime


class MITRELogger:


    def log(self, event):

        return {

            "log_id":

                "MITRELOG-"
                + uuid.uuid4().hex[:8].upper(),


            "event":

                "MITRE intelligence analysis executed",


            "data":

                event,


            "timestamp":

                datetime.utcnow().isoformat()

        }