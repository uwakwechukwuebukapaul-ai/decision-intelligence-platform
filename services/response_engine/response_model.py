from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class ResponseModel:
    """
    Autonomous response execution plan.

    Converts decisions into operational actions.
    """

    response_type: str

    priority: str

    actions: List[str] = field(
        default_factory=list
    )

    execution_state: str = "planned"

    metadata: Dict = field(
        default_factory=dict
    )


    def to_dict(self):

        return {

            "response_type":
                self.response_type,

            "priority":
                self.priority,

            "actions":
                self.actions,

            "execution_state":
                self.execution_state,

            "metadata":
                self.metadata

        }