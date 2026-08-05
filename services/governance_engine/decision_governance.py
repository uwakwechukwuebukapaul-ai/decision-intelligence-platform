from .policy_engine import PolicyEngine
from .approval_manager import ApprovalManager
from .audit_engine import AuditEngine
from .compliance_engine import ComplianceEngine


class DecisionGovernance:
    """
    Main governance controller.

    Ensures every autonomous decision is:

    - policy checked
    - approved
    - audited
    - compliant
    """


    def __init__(self):

        self.policy = PolicyEngine()

        self.approval = ApprovalManager()

        self.audit = AuditEngine()

        self.compliance = ComplianceEngine()



    def govern(
        self,
        decision,
        context=None
    ):


        policy_result = self.policy.evaluate(
            decision,
            context
        )


        approval_result = self.approval.request_approval(
            decision
        )


        compliance_result = self.compliance.validate(
            decision
        )


        audit_result = self.audit.record(
            decision
        )


        return {

            "status":

                "governance_completed",

            "policy":

                policy_result,

            "approval":

                approval_result,

            "compliance":

                compliance_result,

            "audit":

                audit_result

        }