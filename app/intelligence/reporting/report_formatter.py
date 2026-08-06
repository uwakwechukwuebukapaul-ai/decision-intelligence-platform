"""
Sentinel DNA Report Formatter
"""


class ReportFormatter:


    def format_summary(
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


        return (
            f"Indicator {indicator} "
            f"requires investigation. "
            f"Risk level is "
            f"{risk.get('risk','unknown')}."
        )