"""
Sentinel DNA Recommendation Engine

Generates SOC response recommendations.
"""



class RecommendationEngine:



    def recommend(
        self,
        investigation: dict
    ):

        actions = []


        threat = investigation.get(
            "threat_intelligence",
            {}
        )


        severity = investigation.get(
            "incident",
            {}
        ).get(
            "severity",
            "medium"
        )


        threat_level = threat.get(
            "threat_level",
            "low"
        )



        if severity in [
            "critical",
            "high"
        ]:

            actions.append(
                "Block malicious indicator"
            )


        if threat_level == "high":

            actions.append(
                "Perform threat hunting"
            )


        if investigation.get(
            "timeline_count",
            0
        ) > 0:

            actions.append(
                "Collect endpoint telemetry"
            )


        if not actions:

            actions.append(
                "Continue monitoring"
            )


        return actions