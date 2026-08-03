from datetime import datetime


class SecurityReasoner:
    """
    Provides AI security reasoning.
    """


    def reason(
        self,
        event
    ):


        confidence = 70


        reasoning = (
            "Security event requires analysis "
            "based on indicators, severity and context"
        )


        if "ransomware" in event.lower():

            confidence = 95

            reasoning = (
                "Critical ransomware activity detected. "
                "Immediate investigation and containment recommended"
            )



        return {

            "reasoning":
                reasoning,

            "confidence":
                confidence,

            "timestamp":
                datetime.utcnow().isoformat()

        }