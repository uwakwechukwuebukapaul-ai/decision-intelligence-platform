class ExecutiveSummary:
    """
    Generates leadership-level incident summaries.
    """


    def generate(
        self,
        investigation,
        decision
    ):

        return {

            "summary":
            "Security investigation completed",

            "risk":
            "medium",

            "decision":
            decision["decision"]

        }