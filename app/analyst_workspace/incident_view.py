from datetime import datetime


class IncidentView:


    def build(self, incident):

        return {

            "title": "Sentinel DNA Incident Investigation",

            "incident": incident,

            "severity": "critical",

            "sections": [

                "Overview",

                "Evidence",

                "Threat Intelligence",

                "MITRE ATT&CK",

                "Response Actions"

            ],

            "timestamp": datetime.utcnow().isoformat()

        }