class DecisionEngine:


    def decide(
        self,
        reasons
    ):


        decision = "monitor"


        if len(reasons) >= 2:

            decision = "investigate"


        return {

            "decision": decision,

            "priority":
                "high"
                if decision == "investigate"
                else "low"

        }