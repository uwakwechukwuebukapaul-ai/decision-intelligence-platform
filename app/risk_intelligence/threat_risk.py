from datetime import datetime


class ThreatRisk:

    def analyze(self, event):

        text = event.lower()

        score = 20

        if "ransomware" in text:
            score = 40

        if "critical" in text:
            score = 45

        return {
            "threat": event,
            "score": score,
            "severity": "critical"
            if score >= 40 else "medium",
            "timestamp": datetime.utcnow().isoformat()
        }