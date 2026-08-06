"""
Sentinel DNA - Investigation Orchestrator

Coordinates the complete intelligence investigation pipeline.
"""


from datetime import datetime


from app.intelligence.fusion import (
    SentinelIntelligenceEngine,
)


from app.ai.reasoning import (
    ReasoningEngine,
)


from app.ai.copilot import (
    CopilotEngine,
)





class InvestigationOrchestrator:
    """
    Enterprise investigation workflow coordinator.
    """



    def __init__(self):

        self.intelligence_engine = (
            SentinelIntelligenceEngine()
        )


        self.reasoning_engine = (
            ReasoningEngine()
        )


        self.copilot_engine = (
            CopilotEngine()
        )




    def investigate(
        self,
        indicator: str,
    ) -> dict:
        """
        Execute full investigation workflow.
        """


        intelligence = (
            self.intelligence_engine.investigate(
                indicator
            )
        )


        reasoning = (
            self.reasoning_engine.reason(
                intelligence
            )
        )


        copilot = (
            self.copilot_engine.assist(
                intelligence
            )
        )


        return {

            "indicator": indicator,


            "intelligence": intelligence,


            "reasoning": reasoning,


            "copilot": copilot,


            "created_at":
                datetime.utcnow().isoformat(),

        }