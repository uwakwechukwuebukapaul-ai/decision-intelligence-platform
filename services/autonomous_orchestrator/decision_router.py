class DecisionRouter:
    """
    Determines autonomous SOC decision path.
    """


    def route(
        self,
        event
    ):

        event_lower = event.lower()


        priority = "low"


        if any(
            keyword in event_lower
            for keyword in [
                "ransomware",
                "data breach",
                "credential theft",
                "malware"
            ]
        ):

            priority = "critical"


        elif any(
            keyword in event_lower
            for keyword in [
                "phishing",
                "suspicious",
                "exploit"
            ]
        ):

            priority = "high"


        return {

            "priority":
                priority,

            "decision":
                "investigate",

            "autonomous_action":
                True

        }