"""
Sentinel DNA AI Copilot Reasoning Engine

Provides analyst explanations and recommendations.
"""


class CopilotReasoningEngine:


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


        indicator = reputation.get(
            "indicator",
            "unknown",
        )


        severity = risk.get(
            "risk",
            "unknown",
        )


        confidence = reputation.get(
            "confidence",
            0,
        )


        explanation = (
            f"Indicator {indicator} has been classified "
            f"as {severity} risk. "
            f"The assessment confidence is {confidence}%. "
            "The classification was generated using "
            "risk analysis, reputation intelligence, "
            "and threat context."
        )


        recommendations = []


        if severity in (
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


        return {

            "copilot":
                "Sentinel DNA AI Investigation Assistant",


            "explanation":
            {

                "indicator":
                    indicator,

                "severity":
                    severity,

                "confidence":
                    confidence,

                "explanation":
                    explanation,

            },


            "recommendations":
                recommendations,

        }