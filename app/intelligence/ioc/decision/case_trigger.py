"""
Sentinel DNA

IOC Case Trigger

Responsible for deciding when IOC intelligence
should create investigation cases.
"""

from __future__ import annotations



class CaseTrigger:
    """
    Creates case creation instructions.
    """



    def evaluate(
        self,
        decision: dict,
    ) -> dict:
        """
        Evaluate threat decision.
        """


        action = decision.get(
            "action",
            "monitor",
        )


        if action == "create_case":

            return {

                "triggered": True,

                "case_required": True,

                "severity": decision.get(
                    "severity",
                    "high",
                ),

                "reason": decision.get(
                    "reason",
                    "",
                ),

            }



        return {

            "triggered": False,

            "case_required": False,

            "severity": decision.get(
                "severity",
                "low",
            ),

            "reason": decision.get(
                "reason",
                "",
            ),

        }