from datetime import datetime


class RiskReasoner:
    """
    Calculates security risk level.
    """

    def analyze(self, context):

        score = 20

        text = context.lower()


        if "ransomware" in text:
            score += 50


        if "finance" in text:
            score += 20


        if "server" in text or "endpoint" in text:
            score += 10


        if score >= 80:
            level = "critical"

        elif score >= 60:
            level = "high"

        elif score >= 40:
            level = "medium"

        else:
            level = "low"


        return {
            "risk_score": score,
            "risk_level": level,
            "timestamp": datetime.utcnow().isoformat()
        }