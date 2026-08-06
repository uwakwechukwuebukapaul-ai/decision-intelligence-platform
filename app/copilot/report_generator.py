class ReportGenerator:


    def generate_summary(
        self,
        incident
    ):

        indicator = incident.get(
            "indicator",
            "unknown"
        )

        severity = incident.get(
            "severity",
            "unknown"
        )


        return (
            f"Security incident involving "
            f"{indicator} detected with "
            f"{severity} severity."
        )



    def generate_risk(
        self,
        incident
    ):

        severity = incident.get(
            "severity",
            ""
        ).lower()


        if severity == "critical":

            return (
                "Critical risk threat requiring "
                "immediate investigation and response."
            )


        if severity == "high":

            return (
                "High risk threat requiring "
                "security analyst review."
            )


        return (
            "Moderate risk activity requiring monitoring."
        )



    def generate_recommendations(
        self,
        incident
    ):

        return [

            "Block malicious indicators",

            "Review affected assets",

            "Perform threat hunting",

            "Investigate related identities"

        ]