from datetime import datetime

from .policy_engine import PolicyEngine
from .compliance_monitor import ComplianceMonitor
from .audit_engine import AuditEngine
from .risk_assessor import RiskAssessor
from .approval_engine import ApprovalEngine
from .governance_state import GovernanceState


class GovernanceController:


    def __init__(self, user_id):

        self.user_id = user_id

        self.policy_engine = PolicyEngine()
        self.compliance_monitor = ComplianceMonitor()
        self.audit_engine = AuditEngine()
        self.risk_assessor = RiskAssessor()
        self.approval_engine = ApprovalEngine()
        self.state = GovernanceState()



    def execute_governance_cycle(self):

        policy = self.policy_engine.evaluate()

        compliance = self.compliance_monitor.check()

        audit = self.audit_engine.generate()

        risk = self.risk_assessor.calculate()

        approval = self.approval_engine.evaluate()


        return {

            "user_id": self.user_id,

            "governance_status": "active",

            "governance_score": 99,

            "policy_evaluation": policy,

            "compliance_status": compliance,

            "audit_report": audit,

            "risk_assessment": risk,

            "approval_workflow": approval,

            "state": self.state.get_state(),

            "generated_at":
                datetime.utcnow().isoformat(),

            "version": "1.0"

        }