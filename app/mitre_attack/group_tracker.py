from datetime import datetime


class GroupTracker:

    def track(self, event):

        return {
            "groups": [
                "Ransomware Associated Groups"
            ],
            "campaign":
                "Threat Actor Campaign Analysis",
            "timestamp":
                datetime.utcnow().isoformat()
        }