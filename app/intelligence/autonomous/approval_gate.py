"""
Sentinel DNA - Autonomous Approval Gate

Controls human approval boundaries for autonomous actions.

Responsibilities:

- Validate autonomous actions
- Require approval for sensitive operations
- Support analyst-in-the-loop workflows
- Track approval decisions
"""


from __future__ import annotations


from datetime import datetime





class ApprovalGate:
    """
    Human approval control layer for autonomous agents.
    """



    def __init__(self):

        self.name = "sentinel-dna-approval-gate"



    def evaluate(
        self,
        action: str,
        confidence: int = 0,
        risk_level: str = "unknown",
    ) -> dict:
        """
        Determine whether an action requires approval.
        """



        high_risk_actions = [

            "execute",

            "contain",

            "isolate",

            "block",

            "delete"

        ]



        requires_approval = False



        if action.lower() in high_risk_actions:

            requires_approval = True



        if risk_level.lower() in [
            "critical",
            "high"
        ]:

            requires_approval = True



        if confidence < 80:

            requires_approval = True



        status = (
            "pending_approval"
            if requires_approval
            else "approved"
        )



        return {

            "action": action,

            "approval_required": requires_approval,

            "status": status,

            "confidence": confidence,

            "risk_level": risk_level,

            "created_at": datetime.utcnow().isoformat(),

        }




    def request(
        self,
        action: str,
        context: dict | None = None,
    ) -> dict:
        """
        Create an approval request.
        """

        context = context or {}



        return self.evaluate(

            action=action,

            confidence=context.get(
                "confidence",
                0
            ),

            risk_level=context.get(
                "risk",
                "unknown"
            ),

        )