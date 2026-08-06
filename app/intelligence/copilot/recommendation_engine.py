"""
Sentinel DNA

Copilot Recommendation Engine

Generates analyst investigation actions.
"""


class RecommendationEngine:


    def generate(
        self,
        intelligence: dict,
    ) -> list:
        """
        Generate next investigation actions.
        """


        recommendations = []


        risk = intelligence.get(
            "risk",
            {},
        )


        if risk.get("risk") in (
            "high",
            "critical",
        ):

            recommendations.extend(

                [

                    "Search SIEM logs for related activity",

                    "Identify hosts communicating with indicator",

                    "Investigate related indicators",

                    "Consider blocking indicator",

                ]

            )


        else:

            recommendations.append(

                "Monitor indicator activity"

            )


        return recommendations