class RiskDecision:


    def evaluate(self, context):

        indicators = len(
            context.get(
                "threat_indicators",
                []
            )
        )

        if indicators >= 3:
            level = "CRITICAL"

        elif indicators:
            level = "HIGH"

        else:
            level = "LOW"


        return {
            "risk_level": level,
            "confidence": indicators / 5
        }