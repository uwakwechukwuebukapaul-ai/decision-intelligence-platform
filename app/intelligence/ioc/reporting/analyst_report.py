"""
Sentinel DNA

IOC Analyst Report Generator

Transforms IOC intelligence output into
SOC analyst investigation reports.
"""

from __future__ import annotations



class AnalystReportGenerator:
    """
    Generates analyst-focused IOC reports.
    """


    def generate(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Generate investigation report.
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


        threat_context = intelligence.get(
            "threat_context",
            {},
        )


        mitre = intelligence.get(
            "mitre_mapping",
            [],
        )


        severity = risk.get(
            "risk",
            "unknown",
        )


        score = risk.get(
            "score",
            0,
        )


        reasons = risk.get(
            "reasons",
            [],
        )


        recommendations = self._recommendations(
            severity
        )


        return {

            "title": "IOC Investigation Report",

            "indicator": indicator,


            "assessment": {

                "severity": severity,

                "risk_score": score,

                "reasons": reasons,

            },


            "reputation": reputation,


            "threat_context": threat_context,


            "mitre_mapping": mitre,


            "recommendations": recommendations,

        }



    def _recommendations(
        self,
        severity: str,
    ) -> list[str]:
        """
        Generate analyst actions.
        """


        if severity == "high":

            return [

                "Search SIEM logs for related activity",

                "Identify communicating hosts",

                "Investigate related indicators",

                "Consider blocking indicator",

            ]


        if severity == "medium":

            return [

                "Perform additional enrichment",

                "Review historical activity",

            ]


        return [

            "Monitor indicator activity",

            "Collect additional context",

        ]