class ConfidenceEngine:
    """
    Calculates fusion confidence.
    """

    def calculate(
        self,
        signals
    ):

        score = 0


        if signals.get(
            "evidence_signal",
            {}
        ).get(
            "risk_score",
            0
        ):

            score += 40


        if signals.get(
            "detection_signal",
            {}
        ).get(
            "rules"
        ):

            score += 30


        if signals.get(
            "threat_signal"
        ):

            score += 20


        if signals.get(
            "cognitive_signal"
        ):

            score += 10


        return min(
            score,
            100
        )