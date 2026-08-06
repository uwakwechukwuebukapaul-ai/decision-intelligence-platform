"""
Sentinel DNA Investigation Orchestration Engine
"""

from app.intelligence.ioc.fusion import IntelligenceFusion

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


        intelligence = self.fusion.analyze(
            indicator
        )


        result = self.executor.execute(
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
                result,

        }