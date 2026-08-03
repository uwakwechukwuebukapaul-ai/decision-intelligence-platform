from datetime import datetime


class RuleGenerator:

    def generate(self, event):

        return {
            "rules": [
                "Detect suspicious PowerShell execution",
                "Detect ransomware encryption behavior",
                "Detect abnormal process execution"
            ],
            "event": event,
            "timestamp": datetime.utcnow().isoformat()
        }