from datetime import datetime


class CampaignTracker:


    def track(self, threat):

        return {
            "campaign": "Ransomware Campaign Analysis",
            "activity": [
                "Initial Access",
                "Execution",
                "Impact"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }