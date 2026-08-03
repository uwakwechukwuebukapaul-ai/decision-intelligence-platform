from datetime import datetime


class ActionExecutor:

    def prepare(self, automation):

        return {
            "actions": [
                "Isolate affected system",
                "Block malicious indicators",
                "Notify SOC team"
            ],
            "execution_mode": "approval_required",
            "timestamp": datetime.utcnow().isoformat()
        }