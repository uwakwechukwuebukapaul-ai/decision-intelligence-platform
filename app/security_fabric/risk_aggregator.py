from datetime import datetime


class RiskAggregator:


    def calculate(self, alerts, evidence):

        score = 50


        if alerts["confidence"] == "high":
            score += 30


        if len(evidence["entities"]) >= 2:
            score += 20


        level = "medium"


        if score >= 90:
            level = "critical"

        elif score >= 70:
            level = "high"


        return {
            "risk_score": score,
            "risk_level": level,
            "timestamp": datetime.utcnow().isoformat()
        }