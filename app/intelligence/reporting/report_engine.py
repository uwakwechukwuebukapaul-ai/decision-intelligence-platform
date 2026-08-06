"""
Sentinel DNA Investigation Report Engine
"""

from .report_schema import (
    InvestigationReport,
)

from .report_formatter import (
    ReportFormatter,
)


class ReportEngine:

    def __init__(self):

        self.formatter = ReportFormatter()


    def generate(
        self,
        intelligence: dict,
    ):

        risk = intelligence.get(
            "risk",
            {}
        )


        reputation = intelligence.get(
            "reputation",
            {}
        )


        indicator = reputation.get(
            "indicator",
            "unknown"
        )


        summary = self.formatter.format_summary(
            intelligence
        )


        recommendations = [

            "Search SIEM logs for related activity",

            "Identify affected hosts",

            "Review related indicators",

            "Apply containment actions if required",

        ]


        return InvestigationReport(

            indicator=indicator,

            severity=risk.get(
                "risk",
                "unknown"
            ),

            summary=summary,

            technical_analysis=intelligence,

            recommendations=recommendations,

        ).to_dict()