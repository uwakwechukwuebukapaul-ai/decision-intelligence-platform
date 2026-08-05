class HypothesisEngine:
    """
    Creates threat hunting hypotheses.
    """


    def generate(
        self,
        context
    ):

        context = context.lower()

        hypotheses = []


        if "powershell" in context:

            hypotheses.append(
                "Detect malicious PowerShell execution"
            )


        if "ransomware" in context:

            hypotheses.append(
                "Detect ransomware intrusion behavior"
            )


        if "credential" in context:

            hypotheses.append(
                "Detect credential abuse activity"
            )


        if not hypotheses:

            hypotheses.append(
                "Investigate anomalous attacker behavior"
            )


        return hypotheses