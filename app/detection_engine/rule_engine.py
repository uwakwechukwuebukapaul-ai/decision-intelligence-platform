from datetime import datetime


class RuleEngine:


    def evaluate(self, event):

        severity = "low"

        if any(
            keyword in event.lower()
            for keyword in [
                "ransomware",
                "malware",
                "powershell"
            ]
        ):
            severity = "critical"


        return {

            "rule":
                "Suspicious Security Behavior Rule",

            "severity":
                severity,

            "matched":
                True,

            "timestamp":
                datetime.utcnow().isoformat()

        }