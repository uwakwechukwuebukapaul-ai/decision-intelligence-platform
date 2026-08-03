from datetime import datetime


class LogCollector:


    def collect(self, event):

        return {

            "source":
                "Security Telemetry",

            "event":
                event,

            "collection_status":
                "received",

            "timestamp":
                datetime.utcnow().isoformat()

        }