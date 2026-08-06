"""
Sentinel DNA

Investigation Summary Generator

Transforms IOC intelligence into
SOC analyst readable summaries.
"""


class InvestigationSummaryGenerator:
    """
    Generates investigation summaries.
    """


    def generate(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Build analyst investigation summary.
        """


        risk = intelligence.get(
            "risk",
            {},
        )


        reputation = intelligence.get(
            "reputation",
            {},
        )


        return {

            "title": "IOC Investigation Summary",

            "indicator":
                intelligence.get(
                    "indicator",
                    "unknown",
                ),

            "severity":
                risk.get(
                    "risk",
                    "unknown",
                ),

            "risk_score":
                risk.get(
                    "score",
                    0,
                ),

            "confidence":
                reputation.get(
                    "confidence",
                    0,
                ),

            "summary":
                self._build_summary(
                    risk,
                    reputation,
                ),

        }



    def _build_summary(
        self,
        risk: dict,
        reputation: dict,
    ) -> str:
        """
        Generate human-readable analyst explanation.
        """


        severity = risk.get(
            "risk",
            "unknown",
        )


        confidence = reputation.get(
            "confidence",
            0,
        )


        if severity == "high":

            return (
                f"IOC requires investigation. "
                f"Risk level is high with "
                f"{confidence}% confidence."
            )


        return (
            "IOC requires monitoring "
            "and additional analysis."
        )