class SignalProcessor:
    """
    Normalizes intelligence signals from multiple sources.
    """

    def process(
        self,
        event,
        evidence=None,
        detection=None,
        threat=None,
        cognitive=None
    ):

        evidence = evidence or {}
        detection = detection or {}
        threat = threat or {}
        cognitive = cognitive or {}

        signals = {
            "event": event,

            "evidence_signal": {
                "risk_score": evidence.get(
                    "risk_score",
                    0
                )
            },

            "detection_signal": {
                "rules": detection.get(
                    "rules",
                    []
                ),
                "patterns": detection.get(
                    "patterns",
                    []
                )
            },

            "threat_signal": threat,

            "cognitive_signal": cognitive
        }

        return signals