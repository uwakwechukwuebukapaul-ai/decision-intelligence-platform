class ApprovalEngine:
    """
    Autonomous action approval layer.

    Determines whether actions can proceed.
    """


    def __init__(self):

        self.approvals = []


    def evaluate(
        self,
        validation
    ):

        approved = validation.get(
            "valid",
            False
        )


        decision = {

            "approved":
                approved,

            "reason":
                "Validation passed"
                if approved
                else "Validation failed"

        }


        self.approvals.append(
            decision
        )


        return decision


    def history(
        self
    ):

        return self.approvals