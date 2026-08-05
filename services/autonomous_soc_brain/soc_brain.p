from services.investigation_graph_runtime.investigation_planner import (
    InvestigationPlanner
)


class SOCBrain:
    """
    Autonomous SOC reasoning brain.

    Creates investigation strategies
    from security hypotheses.
    """


    def __init__(self):

        self.planner = InvestigationPlanner()



    def reason(
        self,
        hypothesis
    ):

        plan = self.planner.build(
            hypothesis
        )


        return {

            "reasoning": "investigation_strategy_generated",

            "plan": plan

        }