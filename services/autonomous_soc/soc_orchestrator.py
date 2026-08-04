from .analyst_agent import AnalystAgent
from .investigation_planner import InvestigationPlanner


class SOCOrchestrator:
    """
    Coordinates autonomous SOC operations.
    """


    def __init__(self):

        self.agent = AnalystAgent()

        self.planner = InvestigationPlanner()



    def analyze(
        self,
        incident
    ):


        plan = self.planner.create_plan(
            incident
        )


        result = self.agent.investigate(
            incident,
            plan
        )


        return {

            "status":
                "soc_analysis_completed",

            "analysis":
                result.to_dict()

        }