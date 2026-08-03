from datetime import datetime


class RiskCalculator:

    def calculate(
        self,
        threat,
        asset,
        user,
        business
    ):

        score = (
            threat["score"]
            +
            asset["score"]
            +
            user["score"]
            +
            business["score"]
        )

        score = min(score, 100)

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
            "risk_level": level,
            "calculation": [
                "Threat severity",
                "Asset importance",
                "User behavior",
                "Business impact"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }