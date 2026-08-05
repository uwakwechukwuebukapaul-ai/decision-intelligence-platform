from services.investigation_graph_runtime.investigation_planner import (
    InvestigationPlanner
)


class AIInvestigationEngine:
    """
    AI Investigation Engine.

    Coordinates:
    - Investigation planning
    - Hypothesis processing
    - Investigation execution
    """


    def __init__(self):

        self.planner = InvestigationPlanner()



    def investigate(
        self,
        evidence
    ):

        hypothesis = {

            "hypotheses": evidence

        }


        plan = self.planner.build(
            hypothesis
        )


        return {

            "status": "completed",

            "evidence": evidence,

            "plan": plan

        }