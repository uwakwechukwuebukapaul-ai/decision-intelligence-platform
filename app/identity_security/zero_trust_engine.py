from datetime import datetime


class ZeroTrustEngine:
    """
    Zero Trust access evaluation.
    """


    def evaluate(
        self,
        user,
        device,
        risk_score
    ):

        decision = (
            "ALLOW"
            if risk_score < 70
            else
            "BLOCK"
        )


        return {

            "user":
                user,

            "device":
                device,

            "risk_score":
                risk_score,

            "decision":
                decision,

            "principle":
                "Never trust, always verify",

            "timestamp":
                datetime.utcnow().isoformat()

        }