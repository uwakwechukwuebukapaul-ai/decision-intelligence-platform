from datetime import datetime


class ReasoningLayer:
    """
    Performs autonomous security reasoning.
    """

    def reason(self, perception):

        signals = perception.get(
            "signals_detected",
            []
        )

        if "ransomware" in signals:

            conclusion = (
                "Critical ransomware activity "
                "requires immediate containment"
            )

            confidence = 95

        elif signals:

            conclusion = (
                "Suspicious activity detected "
                "requires investigation"
            )

            confidence = 75

        else:

            conclusion = (
                "No significant threat identified"
            )

            confidence = 50


        return {
            "reasoning": conclusion,
            "confidence": confidence,
            "timestamp": datetime.utcnow().isoformat()
        }