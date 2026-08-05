class PriorityEngine:
    """
    Determines autonomous task priority.
    """

    LEVELS = {

        "critical": 4,
        "high": 3,
        "medium": 2,
        "low": 1

    }


    def calculate_priority(
        self,
        severity,
        confidence
    ):

        score = (

            self.LEVELS.get(
                severity,
                1
            )

            +

            confidence

        )


        if score >= 6:
            return "critical"

        if score >= 4:
            return "high"

        if score >= 2:
            return "medium"

        return "low"