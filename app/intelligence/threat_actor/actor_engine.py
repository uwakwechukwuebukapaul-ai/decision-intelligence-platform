"""
Sentinel DNA - Threat Actor Intelligence Engine
"""


from .actor_schema import (
    ThreatActorResult,
)


from .actor_rules import (
    ACTOR_RULES,
)





class ThreatActorEngine:
    """
    Maps intelligence evidence to
    possible threat actor profiles.
    """



    def analyze(
        self,
        intelligence: dict,
    ):


        indicator = intelligence.get(
            "indicator",
            "unknown",
        )


        techniques = []


        for item in intelligence.get(
            "mitre_mapping",
            []
        ):


            techniques.append(
                item.get(
                    "technique_id"
                )
            )




        matches = []

        reasoning = []

        confidence = 0




        for actor in ACTOR_RULES:


            overlap = set(
                techniques
            ).intersection(
                set(actor["techniques"])
            )



            if overlap:


                matches.append(
                    {
                        "name":
                        actor["name"],


                        "confidence":
                        actor["confidence"],


                        "matched_techniques":
                        list(overlap),
                    }
                )


                confidence = max(
                    confidence,
                    actor["confidence"],
                )


                reasoning.extend(
                    actor["reasoning"]
                )





        return ThreatActorResult(

            indicator=indicator,

            actor_match=len(matches) > 0,

            confidence=confidence,

            actors=matches,

            reasoning=list(
                set(reasoning)
            ),

        ).to_dict()