"""
Sentinel DNA Autonomous Security Decision Model.
"""


class SecurityDecisionModel:
    """
    Converts risk intelligence into recommended action.
    """



    def decide(
        self,
        risk_score
    ):


        if risk_score >= 75:

            return {

                "priority":
                    "critical",


                "action":
                    "investigate_immediately",


                "automation":
                    "enabled"

            }


        elif risk_score >= 50:

            return {

                "priority":
                    "high",


                "action":
                    "start_investigation"

            }


        return {

            "priority":
                "medium",


            "action":
                "monitor"

        }