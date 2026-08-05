class DecisionOrchestrator:

    """
    AI decision coordination layer.
    """


    def evaluate(self, investigation):

        return {

            "risk":
                "high"
                if "attack"
                in str(investigation).lower()
                else "medium",

            "recommended_action":
                "investigate_and_contain",

            "confidence":
                0.85
        }