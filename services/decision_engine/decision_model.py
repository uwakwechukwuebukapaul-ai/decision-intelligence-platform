from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class DecisionModel:
    """
    Autonomous decision output contract.
    """

    decision: str

    priority: str

    actions: List[str] = field(
        default_factory=list
    )

    reasoning: Dict = field(
        default_factory=dict
    )


    def to_dict(self):

        return {

            "decision": self.decision,

            "priority": self.priority,

            "actions": self.actions,

            "reasoning": self.reasoning

        }