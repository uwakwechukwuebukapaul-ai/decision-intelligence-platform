from datetime import datetime


class AssetGraph:

    def analyze(self, event):

        return {
            "assets": [
                {
                    "asset": "Finance Database Server",
                    "criticality": "high",
                    "status": "potentially affected"
                }
            ],
            "event": event,
            "timestamp": datetime.utcnow().isoformat()
        }