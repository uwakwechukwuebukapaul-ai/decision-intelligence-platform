"""
Sentinel DNA Investigation State Manager
"""


class InvestigationState:


    STATES = [

        "NEW",

        "ANALYZING",

        "EVIDENCE_COLLECTION",

        "THREAT_ASSESSMENT",

        "DECISION_READY",

        "COMPLETED",

    ]


    def __init__(self):

        self.current_state = "NEW"



    def transition(
        self,
        new_state: str,
    ):


        if new_state not in self.STATES:

            raise ValueError(
                f"Invalid investigation state: {new_state}"
            )


        previous = self.current_state

        self.current_state = new_state


        return {

            "previous_state": previous,

            "current_state": new_state,

            "status": "transition_completed",

        }