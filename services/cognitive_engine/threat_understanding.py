class ThreatUnderstanding:
    """
    Threat interpretation layer.

    Understands:
    - attacker behavior
    - techniques
    - campaigns
    """


    def __init__(self):

        self.understandings = []



    def analyze(
        self,
        threat
    ):

        result = {

            "threat":
                threat,

            "classification":
                "malicious_activity",

            "techniques":
                [
                    "Initial Access",
                    "Execution"
                ],

            "confidence":
                0.88

        }


        self.understandings.append(
            result
        )


        return result



    def history(
        self
    ):

        return self.understandings