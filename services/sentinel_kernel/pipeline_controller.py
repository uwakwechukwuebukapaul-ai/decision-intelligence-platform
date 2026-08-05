class PipelineController:
    """
    Controls the Sentinel DNA investigation pipeline.
    """

    def __init__(
        self,
        router,
        decision_engine
    ):
        self.router = router
        self.decision_engine = decision_engine


    def execute(self, event):

        routing = self.router.route(event)


        intelligence = {
            "event": event,
            "routes": routing["routes"],
            "risk": self.calculate_risk(event)
        }


        decision = self.decision_engine.decide(
            intelligence
        )


        return {
            "routing": routing,
            "intelligence": intelligence,
            "decision": decision
        }


    def calculate_risk(self, event):

        text = str(event).lower()

        if "ransomware" in text:
            return "critical"

        if "malware" in text:
            return "high"

        if "suspicious" in text:
            return "medium"

        return "low"