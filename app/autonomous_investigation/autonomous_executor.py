from .investigation_engine import InvestigationEngine


class AutonomousExecutor:


    def __init__(self):

        self.engine = InvestigationEngine()



    def execute(self, incident):

        investigation = self.engine.investigate(
            incident
        )


        return {

            "status": "completed",

            "investigation":
                investigation,

            "automation":

                {
                    "analysis": "completed",
                    "decision": investigation["decision"],
                    "priority": investigation["priority"]
                }

        }