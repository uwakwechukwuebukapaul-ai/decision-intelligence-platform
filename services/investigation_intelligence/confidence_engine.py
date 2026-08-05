class ConfidenceEngine:
    """
    Calculates confidence in autonomous reasoning.
    """


    def evaluate(
        self,
        investigation
    ):

        confidence = 0.50

        factors = []


        if investigation:

            confidence += 0.20

            factors.append(
                "Investigation completed"
            )


        if "mitre" in investigation:

            confidence += 0.15

            factors.append(
                "MITRE ATT&CK context available"
            )


        if "evidence" in investigation:

            confidence += 0.10

            factors.append(
                "Evidence reasoning available"
            )


        if confidence > 1:

            confidence = 1



        return {

            "confidence":
                round(
                    confidence,
                    2
                ),

            "confidence_factors":
                factors

        }