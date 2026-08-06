"""
Sentinel DNA Analyst Decision Engine

Generates investigation decisions.
"""


class DecisionEngine:


    def analyze(
        self,
        intelligence: dict,
    ):


        risk = intelligence.get(
            "risk",
            {},
        )


        reputation = intelligence.get(
            "reputation",
            {},
        )


        severity = risk.get(
            "risk",
            "unknown",
        )


        confidence = reputation.get(
            "confidence",
            0,
        )



        if severity in (
            "high",
            "critical",
        ):

            action = "investigate"


        else:

            action = "monitor"



        return {


            "decision":

                action,


            "reason":

                f"Indicator severity is {severity} with {confidence}% confidence",


            "confidence":

                confidence,

        }