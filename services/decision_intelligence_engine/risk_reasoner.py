class RiskReasoner:

    def analyze(self, intelligence):
        score = 0

        if isinstance(intelligence, dict):
            score = intelligence.get("risk_score", 0)

        if score >= 80:
            level = "critical"
        elif score >= 60:
            level = "high"
        elif score >= 30:
            level = "medium"
        else:
            level = "low"

        return {
            "risk_score": score,
            "risk_level": level
        }