class ContainmentEngine:
    """
    Autonomous containment decision engine.
    """

    def contain(
        self,
        threat
    ):

        threat_lower = threat.lower()


        actions = []


        if "ransomware" in threat_lower:

            actions = [
                "network isolation",
                "endpoint quarantine",
                "credential lockdown"
            ]


        elif "malware" in threat_lower:

            actions = [
                "endpoint isolation",
                "malware removal",
                "process termination"
            ]


        else:

            actions = [
                "monitor activity",
                "collect additional evidence"
            ]


        return {

            "containment_actions":
                actions,

            "status":
                "containment_ready"

        }