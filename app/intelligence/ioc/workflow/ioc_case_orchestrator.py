"""
Sentinel DNA

IOC Case Orchestrator

Connects IOC intelligence decisions
with investigation workflow.

Responsibilities:
- Consume fused IOC intelligence
- Execute threat decision
- Evaluate case trigger
- Prepare case creation payload
"""

from __future__ import annotations


from app.intelligence.ioc.decision import (
    ThreatDecisionEngine,
    CaseTrigger,
)



class IOCCaseOrchestrator:
    """
    IOC investigation workflow coordinator.
    """



    def __init__(
        self,
    ):

        self.decision_engine = ThreatDecisionEngine()

        self.case_trigger = CaseTrigger()



    def process(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Process IOC intelligence
        and prepare investigation workflow.
        """


        decision = self.decision_engine.decide(
            intelligence
        )


        trigger = self.case_trigger.evaluate(
            decision
        )


        workflow = {

            "workflow": "ioc-investigation",

            "decision": decision,

            "trigger": trigger,

        }


        if trigger.get(
            "case_required"
        ):

            workflow["case"] = self._build_case_payload(
                intelligence,
                decision,
            )


        return workflow



    def _build_case_payload(
        self,
        intelligence: dict,
        decision: dict,
    ) -> dict:
        """
        Prepare case creation payload.
        """


        return {

            "title":
                "Suspicious IOC detected",


            "severity":
                decision.get(
                    "severity",
                    "medium",
                ),


            "source":
                "ioc-intelligence",


            "indicator":
                intelligence.get(
                    "indicator",
                    "unknown",
                ),


            "evidence": {

                "risk":
                    intelligence.get(
                        "risk",
                        {},
                    ),


                "reputation":
                    intelligence.get(
                        "reputation",
                        {}, 
                    ),


                "mitre_mapping":
                    intelligence.get(
                        "mitre_mapping",
                        [],
                    ),

            },

        }