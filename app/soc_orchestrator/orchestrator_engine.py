from services.investigation_graph_runtime.investigation_planner import (
    InvestigationPlanner
)


class OrchestratorEngine:
    """
    SOC orchestration engine.

    Coordinates investigation workflows.
    """


    def __init__(self):

        self.investigation = InvestigationPlanner()



    def execute(
        self,
        incident
    ):

        hypothesis = {

            "hypotheses": [
                incident
            ]

        }


        plan = self.investigation.build(
            hypothesis
        )


        return {

            "status": "completed",

            "incident": incident,

            "investigation_plan": plan

        }