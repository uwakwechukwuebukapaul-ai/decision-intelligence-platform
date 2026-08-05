class DecisionEngine:
    """
    Cognitive Security Decision Engine.

    Generates recommended actions
    from reasoning output.
    """


    def __init__(self):

        self.decisions = []



    def decide(
        self,
        reasoning
    ):

        decision = {

            "recommendation":
                "Investigate and contain threat",

            "reasoning":
                reasoning,

            "confidence":
                0.90

        }


        self.decisions.append(
            decision
        )


        return decision



    def history(
        self
    ):

        return self.decisions