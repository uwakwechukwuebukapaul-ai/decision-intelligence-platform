from datetime import datetime


class IncidentView:
    """
    Generates incident intelligence view.
    """


    def analyze(self, incident):

        text = str(incident).lower()

        severity = "low"

        if "ransomware" in text:
            severity = "critical"

        elif "malware" in text:
            severity = "high"


        return {

            "incident": incident,

            "severity": severity,

            "status": "ACTIVE",

            "recommended_actions": [

                "Collect evidence",

                "Validate indicators",

                "Begin containment"

            ],

            "timestamp":
                datetime.utcnow().isoformat()

        }