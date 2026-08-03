from datetime import datetime


class IncidentView:


    def generate(self, incident):

        return {

            "incident":

                incident,

            "severity":

                "critical"
                if "ransomware" in incident.lower()
                else "medium",

            "status":

                "active investigation",

            "timestamp":

                datetime.utcnow().isoformat()
        }