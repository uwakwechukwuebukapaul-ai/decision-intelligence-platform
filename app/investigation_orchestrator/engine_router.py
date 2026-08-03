from datetime import datetime


class EngineRouter:


    def route(self, event):

        return {

            "engines": [

                "Threat Intelligence",
                "Threat Hunting",
                "Knowledge Graph",
                "Security Analytics",
                "Security Reasoning",
                "AI Copilot",
                "SOAR",
                "Incident Response"

            ],

            "event":
                event,

            "timestamp":
                datetime.utcnow().isoformat()
        }