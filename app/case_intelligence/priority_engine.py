"""
Sentinel DNA Priority Engine

Determines investigation priority.
"""


class PriorityEngine:


    def evaluate(
        self,
        intelligence: dict,
    ):

        risk = intelligence.get(
            "risk",
            {},
        )


        score = risk.get(
            "score",
            0,
        )


        if score >= 90:

            priority = "P1"


        elif score >= 70:

            priority = "P2"


        elif score >= 40:

            priority = "P3"


        else:

            priority = "P4"



        return {

            "priority": priority,

            "risk_score": score,

            "reason":
                f"Risk score {score} determines {priority} priority"

        }