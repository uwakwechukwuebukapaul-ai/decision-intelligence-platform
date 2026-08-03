from datetime import datetime


class ThreatMemory:

    def remember(self, threat):

        return {
            "type": "threat",
            "threat": threat,
            "knowledge": [
                "Threat behavior",
                "Associated techniques",
                "Known indicators"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }