class AutomationController:


    def execute(
        self,
        decision
    ):


        action = decision.get(
            "action"
        )


        if action == "automated_response":

            return {
                "status": "executed",
                "response": "containment initiated"
            }


        return {
            "status": "pending",
            "response": action
        }