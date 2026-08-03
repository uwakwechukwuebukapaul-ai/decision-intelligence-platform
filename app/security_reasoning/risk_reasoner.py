from datetime import datetime


class RiskReasoner:

    def calculate(self, threat):

        if threat["severity"] == "critical":

            score = 100

        else:

            score = 50


        return {
            "risk_score": score,
            "risk_level":
                "critical"
                if score >= 90
                else "medium",
            "timestamp": datetime.utcnow().isoformat()
        }