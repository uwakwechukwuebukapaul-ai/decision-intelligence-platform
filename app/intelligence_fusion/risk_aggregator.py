from datetime import datetime


class RiskAggregator:
    """
    Calculates combined enterprise risk.
    """

    def calculate(self, signals):

        text = str(signals).lower()

        score = 10

        if "ransomware" in text:
            score += 50

        if "critical" in text:
            score += 30

        if "finance" in text:
            score += 20


        if score >= 80:
            level = "critical"

        elif score >= 50:
            level = "high"

        elif score >= 30:
            level = "medium"

        else:
            level = "low"


        return {
            "risk_score": score,
            "risk_level": level,
            "timestamp": datetime.utcnow().isoformat()
        }