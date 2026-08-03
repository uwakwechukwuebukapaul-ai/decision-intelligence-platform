import uuid
from datetime import datetime


class DashboardLogger:


    def log(self, event):

        return {

            "log_id":
                "DASHLOG-"
                + uuid.uuid4().hex[:8].upper(),

            "event":
                "SOC dashboard generated",

            "data":
                event,

            "timestamp":
                datetime.utcnow().isoformat()
        }