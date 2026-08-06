"""
Sentinel DNA Finding Engine

Creates investigation findings.
"""


class FindingEngine:


    def generate(
        self,
        context: dict,
    ):

        findings = []


        incident = context.get(
            "incident",
            {}
        )


        if incident:

            severity = incident.get(
                "severity",
                "unknown"
            )


            findings.append(
                {
                    "type":
                        "severity_assessment",

                    "message":
                        f"Incident severity classified as {severity}"
                }
            )


        evidence = context.get(
            "evidence",
            []
        )


        if evidence:

            findings.append(
                {
                    "type":
                        "evidence",

                    "message":
                        f"{len(evidence)} evidence objects correlated"
                }
            )


        timeline = context.get(
            "timeline",
            []
        )


        if timeline:

            findings.append(
                {
                    "type":
                        "activity",

                    "message":
                        f"{len(timeline)} investigation activities recorded"
                }
            )


        return findings