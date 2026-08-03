from datetime import datetime


class RecoveryPlanner:

    def plan(self, incident):

        return {
            "recovery_actions": [
                "Restore affected systems",
                "Validate security controls",
                "Monitor environment",
                "Return services to operation"
            ],
            "status": "planned",
            "timestamp": datetime.utcnow().isoformat()
        }