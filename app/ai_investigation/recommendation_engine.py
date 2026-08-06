"""
Sentinel DNA Recommendation Engine

Produces SOC response actions.
"""


class RecommendationEngine:


    def generate(
        self,
        context: dict,
    ):


        recommendations = []


        incident = context.get(
            "incident",
            {}
        )


        severity = incident.get(
            "severity"
        )


        if severity in [
            "critical",
            "high"
        ]:

            recommendations.extend(
                [
                    "Block malicious indicator",
                    "Perform threat hunting",
                    "Collect additional telemetry"
                ]
            )


        else:

            recommendations.append(
                "Continue monitoring"
            )


        return recommendations