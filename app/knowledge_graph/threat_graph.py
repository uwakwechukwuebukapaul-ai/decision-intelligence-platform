from datetime import datetime


class ThreatGraph:

    def build(self, incident):

        return {
            "graph": "Threat Relationship Graph",
            "nodes": [
                "Threat Actor",
                "Malware",
                "IOC",
                "Campaign"
            ],
            "incident": incident,
            "timestamp": datetime.utcnow().isoformat()
        }