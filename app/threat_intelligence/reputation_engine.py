from datetime import datetime


class ReputationEngine:


    def score(self, iocs):

        risk = "low"

        if iocs["indicators"]:
            risk = "high"


        return {

            "risk_score":
                85 if risk == "high" else 10,

            "reputation":
                risk,

            "timestamp":
                datetime.utcnow().isoformat()

        }