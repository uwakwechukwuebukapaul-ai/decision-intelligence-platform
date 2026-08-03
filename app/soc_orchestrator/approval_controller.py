from datetime import datetime


class ApprovalController:

    def check(self, priority):

        required = priority == "P1"

        return {
            "approval_required": required,
            "priority": priority,
            "status": (
                "PENDING_APPROVAL"
                if required
                else "AUTO_APPROVED"
            ),
            "timestamp": datetime.now().isoformat()
        }