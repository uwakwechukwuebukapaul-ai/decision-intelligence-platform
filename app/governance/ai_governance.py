from datetime import datetime

from app.governance.decision_explainer import DecisionExplainer
from app.governance.compliance_engine import ComplianceEngine
from app.governance.policy_manager import PolicyManager
from app.governance.risk_assessment import RiskAssessment
from app.governance.governance_memory import GovernanceMemory



class AIGovernance:


    def __init__(self):

        self.explainer = DecisionExplainer()

        self.compliance = ComplianceEngine()

        self.policy = PolicyManager()

        self.risk = RiskAssessment()

        self.memory = GovernanceMemory()



    def evaluate(self, action):


        risk_result = self.risk.assess(action)

        policy_result = self.policy.check(action)

        compliance_result = self.compliance.evaluate(action)


        if risk_result["risk_level"] == "high":

            decision = "BLOCK_PENDING_REVIEW"

            human_review = True

        else:

            decision = "ALLOW_WITH_APPROVAL"

            human_review = True



        result = {


            "action": action,


            "decision": decision,


            "risk": risk_result["risk_level"],


            "confidence": 91,


            "human_review": human_review,


            "policy": policy_result,


            "compliance": compliance_result,


            "explanation":

                self.explainer.explain(action),


            "timestamp":

                datetime.utcnow().isoformat()

        }



        self.memory.store(result)


        return result