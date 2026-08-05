class ApprovalManager:
    """
    Human-in-the-loop approval workflow.
    """

    def __init__(self):

        self.pending = []


    def request(self, action):

        self.pending.append(action)

        return {
            "action": action,
            "status": "pending approval"
        }


    def approve(self, action):

        return {
            "action": action,
            "status": "approved"
        }