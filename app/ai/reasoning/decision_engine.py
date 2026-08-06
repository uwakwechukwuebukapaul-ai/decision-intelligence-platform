"""
Sentinel DNA - Decision Engine

Creates recommended analyst actions.
"""


class DecisionEngine:


    def decide(
        self,
        intelligence: dict,
    ) -> list[str]:


        actions = []


        risk = intelligence.get(
            "risk",
            {}
        )


        score = risk.get(
            "score",
            0
        )


        if score >= 50:

            actions.extend(

                [

                    "Investigate indicator",

                    "Search enterprise telemetry",

                    "Review DNS activity",

                ]

            )


        if intelligence.get(
            "campaign",
            {}
        ).get(
            "campaign_detected"
        ):


            actions.append(
                "Hunt related indicators"
            )


        if intelligence.get(
            "threat_actor",
            {}
        ).get(
            "actor_match"
        ):


            actions.append(
                "Review threat actor techniques"
            )


        if not actions:

            actions.append(
                "Monitor indicator"
            )


        return actions