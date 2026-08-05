class ThreatStoryBuilder:
    """
    Builds analyst-readable investigation narratives.

    Converts raw investigation signals into
    SOC intelligence stories.
    """

    def build(
        self,
        case,
        evidence,
        attack_path,
        techniques
    ):

        return {

            "title":
                "Autonomous Threat Investigation Report",

            "summary":
                self._generate_summary(case),

            "evidence_summary":
                evidence,

            "attack_chain":
                attack_path,

            "mitre_techniques":
                techniques.get(
                    "techniques",
                    []
                ),

            "analyst_view": {

                "what_happened":
                    "Suspicious security activity detected and analyzed",

                "why_it_matters":
                    "Activity matches known adversary behavior patterns",

                "recommended_action":
                    [
                        "Validate affected assets",
                        "Review endpoint telemetry",
                        "Investigate user activity"
                    ]
            }

        }


    def _generate_summary(
        self,
        case
    ):

        if isinstance(case, dict):

            return (
                "Investigation completed for "
                +
                case.get(
                    "alert",
                    "security event"
                )
            )

        return (
            "Investigation completed for "
            +
            str(case)
        )