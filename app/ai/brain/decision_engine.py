from datetime import datetime


class DecisionEngine:


    def make_decision(
        self,
        reasoning
    ):


        confidence = reasoning.get(
            "confidence",
            0
        )


        if confidence >= 70:

            decision = (
                "Proceed with recommended strategy"
            )

        else:

            decision = (
                "Gather additional intelligence"
            )


        return {

            "decision":
                decision,


            "confidence":
                confidence,


            "timestamp":
                datetime.utcnow().isoformat()

        }


    # Backward compatibility
    def decide(
        self,
        reasoning
    ):

        return self.make_decision(
            reasoning
        )