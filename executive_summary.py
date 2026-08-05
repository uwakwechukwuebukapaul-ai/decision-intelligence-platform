class ExecutiveSummary:

    """
    Converts SOC findings into leadership reports.
    """


    def create(
        self,
        investigation,
        decision
    ):

        return {

            "title":
                "Security Incident Summary",

            "impact":
                decision["risk"],

            "status":
                investigation["status"],

            "summary":
                "AI generated incident overview"
        }