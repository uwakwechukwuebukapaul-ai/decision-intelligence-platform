class InvestigationController:


    def start(
        self,
        event,
        intelligence
    ):

        return {

            "status": "investigation_started",

            "event": event,

            "intelligence": intelligence,

            "risk": self.calculate_risk(event)

        }


    def calculate_risk(
        self,
        event
    ):

        severity = event.get(
            "severity",
            "medium"
        )


        if severity == "critical":
            return "high"


        return severity