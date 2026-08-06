"""
Sentinel DNA - Autonomous Decision Manager

Responsible for:

- Evaluating investigation decisions
- Managing autonomous action decisions
- Providing analyst-safe recommendations
- Supporting approval workflows
- Maintaining decision reasoning
"""


from __future__ import annotations


from datetime import datetime


from .autonomous_schema import AutonomousDecisionResult





class AutonomousDecisionManager:
    """
    Controls autonomous investigation decision logic.
    """


    def __init__(self):

        self.name = "sentinel-dna-decision-manager"



    def decide(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Evaluate intelligence and produce a decision.
        """


        indicator = intelligence.get(
            "indicator",
            "unknown"
        )


        risk = intelligence.get(
            "risk",
            {}
        )


        risk_level = risk.get(
            "risk",
            "unknown"
        )


        score = risk.get(
            "score",
            0
        )


        if score >= 80:

            decision = "escalate"

            priority = "critical"


        elif score >= 50:

            decision = "investigate"

            priority = "high"


        else:

            decision = "monitor"

            priority = "low"



        reasoning = [

            f"Indicator {indicator} analyzed",

            f"Risk level evaluated as {risk_level}",

            f"Decision generated: {decision}"

        ]



        result = AutonomousDecisionResult(

            indicator=indicator,

            decision=decision,

            priority=priority,

            confidence=85,

            reasoning=reasoning,

        )



        return {

            "indicator": result.indicator,

            "decision": result.decision,

            "priority": result.priority,

            "confidence": result.confidence,

            "reasoning": result.reasoning,

            "created_at": result.created_at,

        }





    def evaluate(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Alias used by orchestration workflows.
        """

        return self.decide(
            intelligence
        )





# Compatibility export
#
# Existing imports expect:
#
# from app.intelligence.autonomous import DecisionManager
#
# Keep public API stable.

DecisionManager = AutonomousDecisionManager