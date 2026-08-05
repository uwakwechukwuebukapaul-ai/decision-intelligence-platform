class RecommendationEngine:
    """
    Generates analyst response recommendations.
    """


    def recommend(self, findings):

        recommendations = []


        if "ransomware" in findings.lower():

            recommendations.append(
                "Isolate affected hosts immediately"
            )

            recommendations.append(
                "Collect forensic artifacts"
            )


        if "powershell" in findings.lower():

            recommendations.append(
                "Review PowerShell execution logs"
            )


        if not recommendations:

            recommendations.append(
                "Perform additional investigation"
            )


        return recommendations