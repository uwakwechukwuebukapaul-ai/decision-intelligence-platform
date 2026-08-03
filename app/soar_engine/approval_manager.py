from datetime import datetime


class ApprovalManager:
    """
    Controls human approval requirements.
    """


    def check(
        self,
        action
    ):


        approval_required = True


        if "isolate" in action.lower():

            approval_required = True



        return {

            "action":
                action,

            "approval_required":
                approval_required,

            "status":
                "PENDING_APPROVAL"
                if approval_required
                else "APPROVED",

            "timestamp":
                datetime.utcnow().isoformat()

        }