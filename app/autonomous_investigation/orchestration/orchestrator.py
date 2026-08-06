"""
Sentinel DNA Investigation Orchestrator

Coordinates autonomous investigation workflow.

Flow:

Indicator
    |
Intelligence Fusion
    |
Autonomous Investigation Executor
    |
Investigation Result
"""

from __future__ import annotations


from app.intelligence.ioc.fusion import (
    IntelligenceFusion,
)


from app.autonomous_investigation.autonomous_executor import (
    AutonomousExecutor,
)




class InvestigationOrchestrator:


    def __init__(self):

        self.fusion = IntelligenceFusion()

        self.executor = AutonomousExecutor()



    def execute(
        self,
        indicator: str,
    ):

        """
        Execute complete investigation workflow.
        """


        intelligence = self.fusion.analyze(
            indicator
        )


        investigation = self.executor.execute(
            intelligence
        )


        return {

            "workflow":
                "investigation-orchestration",


            "indicator":
                indicator,


            "status":
                "completed",


            "intelligence":
                intelligence,


            "investigation":
                investigation,

        }