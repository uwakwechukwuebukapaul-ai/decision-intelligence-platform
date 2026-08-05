class SelfReasoning:
    """
    Explains autonomous decisions.
    """


    def evaluate(
        self,
        event,
        intelligence,
        decision
    ):

        return {

            "explanation":

                "Decision generated from security intelligence context",

            "confidence":

                "high",

            "decision_trace": {

                "event":

                    event,

                "selected_action":

                    decision.get(
                        "decision",
                        {}
                    )

            }

        }