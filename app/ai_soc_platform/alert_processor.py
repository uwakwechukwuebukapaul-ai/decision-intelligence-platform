from datetime import datetime


class AlertProcessor:


    def process(self, alert):

        return {

            "alert": alert,

            "classification": "Security Incident",

            "severity": "critical",

            "priority": "P1",

            "timestamp": datetime.utcnow().isoformat()

        }