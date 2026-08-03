from datetime import datetime


class ExplanationEngine:

    def explain(self, incident):

        reasons = []

        event = incident.lower()

        if "ransomware" in event:
            reasons.append(
                "Ransomware activity detected"
            )

        if "powershell" in event:
            reasons.append(
                "PowerShell execution detected"
            )

        if "database" in event:
            reasons.append(
                "Critical database asset targeted"
            )

        return {
            "explanation": reasons,
            "confidence": "high",
            "timestamp": datetime.utcnow().isoformat()
        }