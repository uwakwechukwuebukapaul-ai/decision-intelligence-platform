from datetime import datetime


class DecisionKnowledge:
    """
    Converts intelligence into decision recommendations.
    """

    def recommend(self, threat_analysis):

        score = threat_analysis.get(
            "threat_score",
            0
        )

        if score >= 70:

            decision = "Immediate Security Response"

        elif score >= 40:

            decision = "Investigate and Monitor"

        else:

            decision = "Continue Observation"


        return {

            "decision": decision,

            "confidence":
                min(
                    95,
                    score + 20
                ),

            "timestamp":
                datetime.utcnow().isoformat()

        }