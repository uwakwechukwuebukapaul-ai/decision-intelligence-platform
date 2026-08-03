from datetime import datetime


class IntelligenceRouter:


    def collect(self, alert, processed_alert):

        return {

            "sources": [

                "Threat Graph",

                "Knowledge Graph",

                "MITRE ATT&CK",

                "Detection Engineering",

                "Threat Hunting",

                "Risk Intelligence",

                "AI Memory"

            ],

            "severity": processed_alert["severity"],

            "timestamp": datetime.utcnow().isoformat()

        }