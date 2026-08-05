class DecisionTrace:
    """
    Creates explainable AI decision records.
    """


    def record(
        self,
        decision,
        reasoning=None,
        evidence=None
    ):

        return {

            "decision": decision,

            "reasoning": reasoning or [],

            "evidence": evidence or [],

            "trace_status": "recorded"

        }