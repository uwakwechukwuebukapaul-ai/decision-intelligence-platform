"""
Sentinel DNA

IOC Case Orchestrator

Coordinates:
- Threat decision
- Case triggering
- Persistent case creation
"""

from __future__ import annotations


from app.intelligence.ioc.decision import (
    ThreatDecisionEngine,
    CaseTrigger,
)


from app.intelligence.ioc.workflow.services import (
    CaseCreationService,
)



class IOCCaseOrchestrator:
    """
    End-to-end IOC investigation workflow.
    """


    def __init__(
        self,
    ):

        self.decision_engine = ThreatDecisionEngine()

        self.case_trigger = CaseTrigger()

        self.case_creator = CaseCreationService()



    def process(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Execute IOC investigation workflow.
        """


        decision = self.decision_engine.decide(
            intelligence
        )


        trigger = self.case_trigger.evaluate(
            decision
        )


        result = {

            "workflow": "ioc-investigation",

            "decision": decision,

            "trigger": trigger,

        }



        if trigger.get(
            "case_required"
        ):

            case = self.case_creator.create_case(
                intelligence
            )


            result["case"] = case


        else:

            result["case"] = None



        return result