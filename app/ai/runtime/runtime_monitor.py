from datetime import datetime


class RuntimeMonitor:


    def get_status(self):

        return {

            "runtime":
                "active",

            "timestamp":
                datetime.utcnow().isoformat()

        }