"""
Sentinel DNA - Explanation Engine

Produces analyst-readable reasoning.
"""


class ExplanationEngine:


    def explain(
        self,
        intelligence: dict,
        hypothesis: dict,
    ) -> str:


        indicator = intelligence.get(
            "indicator",
            "unknown"
        )


        confidence = hypothesis.get(
            "confidence",
            0
        )


        return (

            f"Indicator {indicator} was analyzed "
            f"using multiple intelligence sources. "
            f"The investigation hypothesis is "
            f"'{hypothesis['hypothesis']}' "
            f"with {confidence}% confidence."

        )