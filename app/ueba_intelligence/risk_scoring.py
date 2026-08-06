class RiskScoring:


    def calculate(
        self,
        anomalies
    ):

        score = 20


        if anomalies:

            score = 80


        level = "low"


        if score >= 80:

            level = "high"


        elif score >= 90:

            level = "critical"


        return {

            "risk_score": score,

            "risk_level": level

        }