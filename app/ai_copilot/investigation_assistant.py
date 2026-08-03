from datetime import datetime


class InvestigationAssistant:

    def assist(self, incident):

        return {
            "investigation_steps": [
                "Analyze security evidence",
                "Review attack timeline",
                "Identify affected assets",
                "Validate attacker behavior"
            ],
            "incident": incident,
            "timestamp": datetime.utcnow().isoformat()
        }