from datetime import datetime


class ReputationEngine:
    """
    Calculates IOC reputation.
    """


    def analyze(
        self,
        indicator
    ):

        malicious = any(

            keyword in indicator.lower()

            for keyword in [

                "malware",
                "ransomware",
                "phishing",
                "evil"

            ]

        )


        score = 90 if malicious else 10


        return {

            "indicator":
                indicator,

            "reputation_score":
                score,

            "classification":
                "malicious"
                if malicious
                else
                "unknown",

            "timestamp":
                datetime.utcnow().isoformat()

        }