from datetime import datetime


class ContextBuilder:


    def build(self, incident):

        return {

            "incident": incident,

            "available_intelligence": [

                "Threat Graph",

                "Knowledge Graph",

                "MITRE ATT&CK",

                "Risk Intelligence",

                "AI Memory"

            ],

            "timestamp": datetime.utcnow().isoformat()

        }