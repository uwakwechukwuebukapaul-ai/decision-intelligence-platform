import uuid
from datetime import datetime

from .reasoning_engine import ReasoningEngine
from .decision_engine import DecisionEngine
from .investigation_repository import InvestigationRepository



class InvestigationEngine:


    def __init__(self):

        self.reasoning = ReasoningEngine()

        self.decision = DecisionEngine()

        self.repository = InvestigationRepository()



    def investigate(
        self,
        incident
    ):


        reasons = self.reasoning.analyze(
            incident
        )


        decision = self.decision.decide(
            reasons
        )


        result = {


            "investigation_id":
            "INV-" + uuid.uuid4().hex[:8].upper(),


            "incident_id":
            incident.get(
                "incident_id"
            ),


            "indicator":
            incident.get(
                "indicator"
            ),


            "reasons":
            reasons,


            "decision":
            decision["decision"],


            "priority":
            decision["priority"],


            "confidence":
            0.90,


            "created_at":
            datetime.utcnow().isoformat()

        }


        self.repository.save(
            result
        )


        return result