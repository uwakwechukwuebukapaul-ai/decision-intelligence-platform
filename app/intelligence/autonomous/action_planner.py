"""
Sentinel DNA - Autonomous Action Planner
"""


from __future__ import annotations



class ActionPlanner:
    """
    Generates investigation actions.
    """


    def plan(
        self,
        intelligence: dict,
    ) -> list[str]:


        actions = []


        risk = intelligence.get(
            "risk",
            {}
        )


        if risk.get("risk") == "high":

            actions.extend(
                [
                    "Collect DNS intelligence",
                    "Search endpoint telemetry",
                    "Review related indicators",
                    "Map MITRE techniques",
                ]
            )


        else:

            actions.append(
                "Continue monitoring"
            )


        return actions