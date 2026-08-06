"""
Sentinel DNA Escalation Engine
"""


class EscalationEngine:



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


            level = "critical"

            escalate = True



        elif score >= 70:


            level = "high"

            escalate = True



        else:


            level = "normal"

            escalate = False




        return {


            "escalation_level":

                level,


            "requires_escalation":

                escalate,


            "score":

                score,

        }