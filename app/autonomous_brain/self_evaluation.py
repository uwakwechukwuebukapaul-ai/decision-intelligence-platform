from datetime import datetime


class SelfEvaluation:
    """
    Evaluates AI decision quality.
    """

    def evaluate(self, result):

        confidence = (
            result
            .get("reasoning", {})
            .get("confidence", 0)
        )


        if confidence >= 90:

            status = "high_quality"

        elif confidence >= 70:

            status = "acceptable"

        else:

            status = "needs_improvement"


        return {

            "evaluation":
                status,

            "confidence":
                confidence,

            "timestamp":
                datetime.utcnow().isoformat()
        }