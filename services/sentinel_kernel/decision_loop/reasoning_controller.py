class ReasoningController:
    """
    Sentinel DNA AI reasoning coordinator.

    Combines multiple intelligence sources
    into a unified security understanding.
    """

    def reason(
        self,
        context
    ):

        intelligence = context.intelligence

        risk = "LOW"

        indicators = []

        if intelligence:

            indicators = intelligence.get(
                "indicators",
                []
            )

            reputation = intelligence.get(
                "reputation",
                {}
            )

            risk = reputation.get(
                "risk_level",
                "LOW"
            )


        reasoning = {

            "threat_assessment":
                risk,

            "indicators":
                indicators,

            "confidence":
                self.calculate_confidence(
                    indicators
                ),

            "recommendation":
                self.generate_recommendation(
                    risk
                )
        }


        context.update_analysis(
            reasoning
        )


        return reasoning


    def calculate_confidence(
        self,
        indicators
    ):

        if len(indicators) >= 3:
            return "HIGH"

        if len(indicators) > 0:
            return "MEDIUM"

        return "LOW"


    def generate_recommendation(
        self,
        risk
    ):

        if risk == "HIGH":

            return "Initiate incident response workflow"


        return "Continue monitoring"