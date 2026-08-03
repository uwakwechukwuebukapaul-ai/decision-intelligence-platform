from datetime import datetime


class DecisionEngine:

    def evaluate(self, incident):

        severity = "critical" if any(
            word in incident.lower()
            for word in [
                "ransomware",
                "malware",
                "breach",
                "data"
            ]
        ) else "medium"

        priority = (
            "P1"
            if severity == "critical"
            else "P3"
        )

        return {
            "severity": severity,
            "priority": priority,
            "decision": "Immediate SOC response required",
            "timestamp": datetime.now().isoformat()
        }