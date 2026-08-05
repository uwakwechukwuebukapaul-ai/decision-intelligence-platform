class HypothesisManager:
    """
    Generates and manages investigation hypotheses.
    """

    def create(self, evidence):

        hypotheses = []

        findings = evidence.get(
            "findings",
            []
        )

        if "Network indicator identified" in findings:
            hypotheses.append(
                "Possible command and control communication"
            )

        if "Suspicious domain detected" in findings:
            hypotheses.append(
                "Possible phishing or malware delivery"
            )

        return {
            "hypotheses": hypotheses,
            "confidence": self.calculate_confidence(
                hypotheses
            )
        }


    def calculate_confidence(self, hypotheses):

        if not hypotheses:
            return 0

        return min(
            95,
            len(hypotheses) * 40
        )