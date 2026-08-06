"""
Decision Policy

Controls how the planner
selects investigation actions.
"""


class DecisionPolicy:
    """
    Basic rule-based decision policy.

    Future:
    - LLM reasoning
    - threat models
    - confidence scoring
    """


    def choose_capabilities(
        self,
        objective: str,
    ) -> list[str]:

        objective = objective.lower()


        capabilities = []


        if "threat" in objective:
            capabilities.append(
                "threat_intelligence"
            )


        if "risk" in objective:
            capabilities.append(
                "risk_analysis"
            )


        if "investigation" in objective:
            capabilities.append(
                "investigation"
            )


        if not capabilities:

            capabilities.append(
                "threat_intelligence"
            )


        return capabilities