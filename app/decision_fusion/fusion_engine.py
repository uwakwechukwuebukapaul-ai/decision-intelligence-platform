from datetime import datetime

from .risk_fusion import RiskFusion
from .decision_repository import DecisionRepository



class FusionEngine:


    def __init__(self):

        self.risk_engine = RiskFusion()

        self.repository = DecisionRepository()



    def evaluate(self, context):


        risk = self.risk_engine.calculate(
            context
        )


        if risk["risk_level"] == "critical":

            decision = "immediate_response"

            actions = [

                "Execute SOAR playbook",

                "Isolate affected asset",

                "Investigate identity activity"

            ]


        elif risk["risk_level"] == "high":

            decision = "investigate"

            actions = [

                "Perform threat hunting",

                "Collect additional evidence"

            ]


        else:

            decision = "monitor"

            actions = [

                "Continue observation"

            ]



        result = {

            "decision_id":
                self.repository.generate_id(),

            "risk_score":
                risk["risk_score"],

            "risk_level":
                risk["risk_level"],

            "decision":
                decision,

            "signals":
                risk["findings"],

            "recommended_actions":
                actions,

            "confidence":
                0.94,

            "created_at":
                datetime.utcnow().isoformat()

        }


        return self.repository.save(result)