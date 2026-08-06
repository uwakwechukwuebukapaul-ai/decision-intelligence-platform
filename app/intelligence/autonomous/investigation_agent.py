"""
Sentinel DNA - Autonomous Investigation Agent
"""


from __future__ import annotations



from .action_planner import ActionPlanner
from .evidence_collector import EvidenceCollector



class InvestigationAgent:


    def __init__(self):

        self.planner = ActionPlanner()

        self.collector = EvidenceCollector()



    def execute(
        self,
        intelligence: dict,
    ):


        actions = self.planner.plan(
            intelligence
        )


        evidence = self.collector.collect(
            intelligence
        )


        return {

            "actions": actions,

            "evidence": evidence,

            "reasoning": [
                "Risk assessment completed",
                "Investigation workflow generated",
            ]

        }