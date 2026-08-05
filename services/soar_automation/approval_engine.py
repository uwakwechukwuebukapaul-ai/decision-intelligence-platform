class ApprovalEngine:
    """
    Governance layer for human approval.

    Prevents unsafe automation.
    """

    def requires_approval(self, action):

        sensitive_actions = [
            "disable_account",
            "shutdown_system"
        ]

        return action in sensitive_actions

    def approve(self, action, analyst):

        return {
            "action": action,
            "approved_by": analyst,
            "status": "approved"
        }