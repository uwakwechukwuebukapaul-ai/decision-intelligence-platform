class AnalystSummary:
    """
    Produces analyst-facing summaries.
    """


    def summarize(
        self,
        report
    ):

        risk = report.get(
            "risk_assessment",
            {}
        )


        return {

            "summary":
                (
                    "Autonomous investigation completed. "
                    "Risk level: "
                    +
                    risk.get(
                        "risk_level",
                        "UNKNOWN"
                    )
                ),

            "recommended_actions":[

                "Review affected assets",

                "Collect endpoint telemetry",

                "Validate suspicious activity"

            ]

        }