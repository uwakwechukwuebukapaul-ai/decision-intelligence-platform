"""
Sentinel DNA Response Agent

Generates recommended SOC actions.
"""


from .base_agent import BaseAgent



class ResponseAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "ResponseAgent"
        )


    def analyze(
        self,
        investigation
    ):


        risk = (
            investigation.state.risk_score
        )


        actions = []


        if risk >= 70:

            actions.extend(
                [
                    "Isolate affected asset",
                    "Block malicious indicators",
                    "Escalate incident"
                ]
            )


        elif risk >= 40:

            actions.extend(
                [
                    "Investigate indicators",
                    "Monitor affected accounts"
                ]
            )


        else:

            actions.append(
                "Continue monitoring"
            )


        result = {

            "agent":
                self.name,

            "recommended_actions":
                actions

        }


        for action in actions:

            investigation.add_finding(
                action
            )


        return result