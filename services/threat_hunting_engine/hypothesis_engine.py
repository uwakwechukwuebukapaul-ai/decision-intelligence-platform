class HypothesisEngine:
    """
    Generates threat hunting hypotheses.

    Mimics senior SOC analyst reasoning.
    """

    def generate(self, context):
        hypotheses = []

        text = str(context).lower()

        if "login" in text or "authentication" in text:
            hypotheses.append(
                "Investigate possible credential abuse or account compromise"
            )

        if "powershell" in text:
            hypotheses.append(
                "Investigate possible command execution activity"
            )

        if "network" in text or "connection" in text:
            hypotheses.append(
                "Investigate suspicious network communication"
            )

        if not hypotheses:
            hypotheses.append(
                "Perform general threat discovery analysis"
            )

        return hypotheses