class DecisionRouter:


    def evaluate(
        self,
        event,
        investigation
    ):

        risk = investigation.get(
            "risk",
            "medium"
        )


        if risk == "high":

            return {
                "action": "automated_response",
                "priority": "critical"
            }


        if risk == "medium":

            return {
                "action": "analyst_investigation",
                "priority": "high"
            }


        return {
            "action": "monitor",
            "priority": "low"
        }