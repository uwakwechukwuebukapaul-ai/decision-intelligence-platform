"""
Sentinel DNA

Copilot Explanation Engine

Converts security intelligence
into analyst-readable explanations.
"""


class ExplanationEngine:


    def explain(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Generate investigation explanation.
        """


        indicator = intelligence.get(
            "indicator",
            "unknown",
        )


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


        explanation = (

            f"Indicator {indicator} "
            f"has been classified as {severity} risk. "

            f"The assessment confidence is "
            f"{confidence}%. "

            "The classification was generated "
            "using risk analysis, reputation "
            "intelligence, and threat context."

        )


        return {

            "indicator": indicator,

            "severity": severity,

            "confidence": confidence,

            "explanation": explanation,

        }