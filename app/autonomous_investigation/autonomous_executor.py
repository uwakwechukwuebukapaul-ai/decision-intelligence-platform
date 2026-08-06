"""
Sentinel DNA Autonomous Investigation Executor
"""


from .investigation_planner import (
    InvestigationPlanner,
)

from .evidence_collector import (
    EvidenceCollector,
)

from .investigation_agent import (
    InvestigationAgent,
)



class AutonomousExecutor:



    def __init__(self):

        self.planner = InvestigationPlanner()

        self.collector = EvidenceCollector()

        self.agent = InvestigationAgent()



    def execute(
        self,
        intelligence: dict,
    ):


        plan = self.planner.create_plan(
            intelligence
        )


        evidence = self.collector.collect(
            intelligence
        )


        result = self.agent.investigate(

            intelligence,

            plan,

            evidence,

        )


        return {


            "workflow":

                "autonomous-investigation",


            "result":

                result,

        }