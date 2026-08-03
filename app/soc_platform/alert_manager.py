from datetime import datetime


class AlertManager:


    def analyze(self, alert):


        text = str(alert).lower()


        severity = "medium"
        priority = "P3"


        if any(
            item in text
            for item in [
                "ransomware",
                "critical",
                "data breach"
            ]
        ):

            severity = "critical"
            priority = "P1"


        elif "malware" in text:

            severity = "high"
            priority = "P2"



        return {

            "alert":
                alert,

            "severity":
                severity,

            "priority":
                priority,

            "category":
                "Security Incident",

            "timestamp":
                datetime.utcnow().isoformat()

        }