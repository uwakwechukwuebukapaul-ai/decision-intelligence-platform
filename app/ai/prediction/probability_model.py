from datetime import datetime


class ProbabilityModel:

    def calculate(
        self,
        signals
    ):

        score = 50

        if signals:

            score += len(signals) * 10

        probability = min(
            score,
            95
        )

        return {

            "probability": probability,

            "confidence_level":
                "high"
                if probability >= 80
                else "medium",

            "timestamp":
                datetime.utcnow().isoformat()

        }