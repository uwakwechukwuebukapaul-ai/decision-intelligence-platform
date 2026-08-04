from .base_agent import BaseAgent


class IncidentCommanderAgent(BaseAgent):
    """
    Coordinates incident decisions.
    """


    def __init__(self):

        super().__init__(
            "incident_commander"
        )


    def execute(
        self,
        context
    ):

        risk = context.get(
            "risk_score",
            0
        )


        if risk >= 90:

            priority = "critical"

            action = "contain immediately"


        elif risk >= 50:

            priority = "high"

            action = "investigate"


        else:

            priority = "low"

            action = "monitor"



        return {

            "agent":
                self.name,

            "priority":
                priority,

            "recommended_action":
                action,

            "timestamp":
                self.timestamp()

        }