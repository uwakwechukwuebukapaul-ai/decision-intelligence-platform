from datetime import datetime


class BusinessImpact:

    def calculate(self, event):

        text = event.lower()

        score = 10
        impact = "low"

        if "finance" in text:
            score = 30
            impact = "high"

        if "database" in text:
            score = 35
            impact = "critical"

        return {
            "impact_level": impact,
            "score": score,
            "affected_department": "Enterprise Operations",
            "timestamp": datetime.utcnow().isoformat()
        }