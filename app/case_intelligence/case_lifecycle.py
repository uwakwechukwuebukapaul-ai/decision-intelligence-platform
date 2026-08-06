"""
Sentinel DNA Case Lifecycle Manager
"""


class CaseLifecycle:



    STATES = [

        "OPEN",

        "TRIAGED",

        "INVESTIGATING",

        "CONTAINMENT",

        "RESOLVED",

        "CLOSED",

    ]



    def transition(
        self,
        current: str,
        target: str,
    ):


        if target not in self.STATES:


            raise ValueError(
                "Invalid lifecycle state"
            )



        return {


            "previous_state":

                current,


            "current_state":

                target,


            "status":

                "transition_completed",

        }