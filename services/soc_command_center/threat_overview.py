class ThreatOverview:
    """
    Displays current threat landscape.
    """


    def analyze(
        self,
        threats=None
    ):

        threats = threats or []


        return {

            "status": "threat_overview_generated",

            "total_threats": len(threats),

            "critical_threats":

                [
                    threat

                    for threat in threats

                    if threat.get(
                        "severity"
                    ) == "critical"

                ]

        }