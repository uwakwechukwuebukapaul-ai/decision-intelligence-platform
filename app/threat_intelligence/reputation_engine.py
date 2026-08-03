from datetime import datetime


class ReputationEngine:


    def check(self, enrichment):

        risk = "low"


        if len(
            enrichment["enriched_indicators"]
        ) >= 2:

            risk = "critical"


        return {
            "reputation": risk,
            "confidence": "high",
            "timestamp": datetime.utcnow().isoformat()
        }