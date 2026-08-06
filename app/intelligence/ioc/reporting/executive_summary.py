"""
Sentinel DNA

IOC Executive Summary Generator

Creates management-level security summaries.
"""

from __future__ import annotations



class ExecutiveSummaryGenerator:
    """
    Generates executive security summaries.
    """



    def generate(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Generate executive summary.
        """


        indicator = intelligence.get(
            "indicator",
            "unknown",
        )


        risk = intelligence.get(
            "risk",
            {},
        )


        severity = risk.get(
            "risk",
            "unknown",
        )


        score = risk.get(
            "score",
            0,
        )


        if severity == "high":

            verdict = (
                "Indicator shows characteristics "
                "associated with potential malicious activity."
            )


        elif severity == "medium":

            verdict = (
                "Indicator requires additional investigation."
            )


        else:

            verdict = (
                "Indicator currently presents limited risk."
            )



        return {

            "indicator": indicator,

            "severity": severity,

            "risk_score": score,

            "verdict": verdict,

            "business_impact": self._impact(
                severity
            ),

        }



    def _impact(
        self,
        severity: str,
    ) -> str:

        impacts = {

            "high":
                "Potential compromise or malicious communication risk.",

            "medium":
                "Requires monitoring and validation.",

            "low":
                "Low immediate security concern.",

        }


        return impacts.get(
            severity,
            "Unknown impact.",
        )