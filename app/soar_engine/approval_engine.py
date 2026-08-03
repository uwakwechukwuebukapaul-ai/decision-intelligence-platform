from datetime import datetime


class ApprovalEngine:

    def approve(self, action):

        return {
            "action": action,
            "approval": "approved",
            "approved_by": "SOC Analyst",
            "timestamp": datetime.utcnow().isoformat()
        }