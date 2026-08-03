from datetime import datetime


class AssetGraph:

    def build(self, incident):

        return {
            "assets": [
                "Endpoint",
                "Database Server",
                "User Account"
            ],
            "impact": "high",
            "incident": incident,
            "timestamp": datetime.utcnow().isoformat()
        }