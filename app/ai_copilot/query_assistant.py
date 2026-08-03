from datetime import datetime


class QueryAssistant:

    def generate(self, incident):

        return {
            "queries": [
                "Search PowerShell execution logs",
                "Find suspicious process activity",
                "Identify abnormal network connections",
                "Review endpoint telemetry"
            ],
            "formats": [
                "KQL",
                "Splunk SPL",
                "Elastic Query"
            ],
            "timestamp":
                datetime.utcnow().isoformat()
        }