from datetime import datetime


class RiskScorer:


    def score(self, event):

        event_lower = event.lower()

        score = 40

        if "ransomware" in event_lower:
            score += 40

        if "powershell" in event_lower:
            score += 15

        if "database" in event_lower:
            score += 5


        level = "medium"

        if score >= 90:
            level = "critical"
        elif score >= 70:
            level = "high"


        return {

            "risk_score": score,

            "risk_level": level,

            "timestamp":
                datetime.utcnow().isoformat()

        }