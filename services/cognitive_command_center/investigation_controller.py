class InvestigationController:
    """
    Controls investigation workflows.

    Coordinates investigation execution,
    evidence collection and analyst actions.
    """

    def __init__(self):

        self.active_investigations = []


    def run(self, case):

        investigation = {

            "case": case,

            "status": "investigation_started",

            "steps": [

                "collect_evidence",

                "analyze_threat_context",

                "generate_recommendations"

            ]

        }


        self.active_investigations.append(
            investigation
        )


        return investigation


    def get_active_cases(self):

        return self.active_investigations