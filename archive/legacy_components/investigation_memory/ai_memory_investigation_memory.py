from datetime import datetime


class InvestigationMemory:

    def store_investigation(self, investigation):

        return {
            "type": "investigation",
            "case": investigation,
            "learned_actions": [
                "Evidence collection",
                "IOC analysis",
                "Timeline reconstruction"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }