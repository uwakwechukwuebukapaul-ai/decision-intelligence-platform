class PredictionEngine:

    def predict(self, context):

        risk = "low"

        if isinstance(context, dict):

            score = context.get(
                "risk_score",
                0
            )

            if score >= 80:
                risk = "high"

            elif score >= 40:
                risk = "medium"


        return {
            "risk": risk,
            "source": "prediction_engine"
        }