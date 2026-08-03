from datetime import datetime


class ConfidenceReasoner:
    """
    Evaluates reasoning confidence.
    """

    def calculate(
        self,
        risk,
        reasoning
    ):

        confidence = 70


        if risk["risk_score"] > 70:
            confidence += 15


        if len(
            reasoning.get(
                "reasoning_steps",
                []
            )
        ) > 2:

            confidence += 10


        return {

            "confidence":
                min(
                    confidence,
                    99
                ),

            "timestamp":
                datetime.utcnow().isoformat()

        }