class ConfidenceCalculator:
    """
    Calculates investigation confidence.

    Future:
    - ML model scoring
    - historical accuracy
    - analyst feedback
    """


    def calculate(
        self,
        evidence
    ):


        if not evidence:

            return 0



        total = sum(

            item.get(
                "weight",
                0
            )

            for item in evidence

        )


        confidence = total / len(evidence)



        if confidence > 100:

            confidence = 100



        return round(
            confidence,
            2
        )