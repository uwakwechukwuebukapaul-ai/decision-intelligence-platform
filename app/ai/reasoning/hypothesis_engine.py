"""
Sentinel DNA - Hypothesis Engine

Generates investigation hypotheses.
"""


class HypothesisEngine:


    def generate(
        self,
        intelligence: dict,
    ) -> dict:


        risk = intelligence.get(
            "risk",
            {}
        )


        threat = intelligence.get(
            "threat_actor",
            {}
        )


        campaign = intelligence.get(
            "campaign",
            {}
        )


        score = risk.get(
            "score",
            0
        )


        if campaign.get(
            "campaign_detected"
        ):


            return {

                "hypothesis":
                    "Possible coordinated threat campaign",

                "confidence":
                    80,

            }



        if threat.get(
            "actor_match"
        ):


            return {

                "hypothesis":
                    "Possible threat actor infrastructure",

                "confidence":
                    75,

            }



        if score >= 70:


            return {

                "hypothesis":
                    "High risk malicious indicator",

                "confidence":
                    70,

            }



        return {

            "hypothesis":
                "Suspicious indicator requiring investigation",

            "confidence":
                50,

        }