"""
Intelligence Planner

Creates investigation strategies
from security objectives.
"""

from .decision_policy import DecisionPolicy
from .investigation_strategy import InvestigationStrategy


class IntelligencePlanner:
    """
    Autonomous investigation planner.
    """


    def __init__(
        self,
        policy=None,
    ):

        self.policy = (
            policy
            or DecisionPolicy()
        )


    def create_strategy(
        self,
        objective: str,
    ) -> InvestigationStrategy:


        capabilities = (
            self.policy.choose_capabilities(
                objective
            )
        )


        strategy = InvestigationStrategy(
            objective=objective
        )


        for capability in capabilities:

            strategy.add_capability(
                capability
            )


        return strategy