class ExplanationEngine:
    """
    Converts security signals into analyst explanations.
    """

    def explain(self, alert):

        return {
            "alert": alert,
            "explanation": (
                "This alert requires investigation "
                "based on available security indicators."
            ),
            "analysis": {
                "risk_factors": [],
                "confidence": "medium"
            }
        }