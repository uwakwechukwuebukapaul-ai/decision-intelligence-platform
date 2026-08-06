"""
Sentinel DNA - Autonomous Investigation Engine

Coordinates autonomous investigation workflows.

Responsibilities:

- Execute autonomous investigations
- Coordinate investigation agents
- Transform execution results
- Produce structured investigation output
"""


from __future__ import annotations


from .investigation_agent import InvestigationAgent
from .autonomous_schema import AutonomousInvestigationResult





class AutonomousInvestigationEngine:
    """
    Core autonomous investigation workflow engine.
    """


    def __init__(self):

        self.agent = InvestigationAgent()



    def investigate(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Run autonomous investigation workflow.
        """


        indicator = intelligence.get(
            "indicator"
        )


        execution = self.agent.execute(
            intelligence
        )


        result = AutonomousInvestigationResult(

            indicator=indicator,

            status="investigation_ready",

            confidence=85,

            actions=execution.get(
                "actions",
                []
            ),

            evidence=execution.get(
                "evidence",
                {}
            ),

            reasoning=execution.get(
                "reasoning",
                []
            )

        )


        return {

            "indicator": result.indicator,

            "status": result.status,

            "confidence": result.confidence,

            "actions": result.actions,

            "evidence": result.evidence,

            "reasoning": result.reasoning,

            "created_at": result.created_at,

        }




    def run(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Execution alias for orchestration layers.
        """

        return self.investigate(
            intelligence
        )





# Compatibility export
#
# Existing modules expect:
#
# from app.intelligence.autonomous import AutonomousEngine
#
# Keep old interface stable.

AutonomousEngine = AutonomousInvestigationEngine