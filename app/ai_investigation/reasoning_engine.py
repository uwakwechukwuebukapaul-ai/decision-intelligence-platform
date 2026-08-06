"""
Sentinel DNA Reasoning Engine

Explains investigation decisions.
"""


class ReasoningEngine:


    def analyze(
        self,
        context: dict,
    ):


        reasons = []


        incident = context.get(
            "incident",
            {}
        )


        severity = incident.get(
            "severity"
        )


        if severity in [
            "high",
            "critical"
        ]:

            reasons.append(
                "High severity incident requires investigation"
            )


        if incident.get(
            "indicator"
        ):

            reasons.append(
                "IOC indicator detected"
            )


        if context.get(
            "timeline"
        ):

            reasons.append(
                "Investigation activity recorded"
            )


        return reasons