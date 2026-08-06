"""
Sentinel DNA Analyst Recommendation Engine
"""


class AnalystRecommendationEngine:



    def generate(
        self,
        intelligence: dict,
    ):


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

                    "Search SIEM logs for indicator activity",

                    "Identify affected hosts",

                    "Review related network connections",

                    "Consider blocking indicator",

                ]

            )


        else:


            recommendations.append(

                "Continue monitoring indicator"

            )



        return recommendations