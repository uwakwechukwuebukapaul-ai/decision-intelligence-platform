from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class WorkflowModel:
    """
    Autonomous SOC workflow object.

    Tracks the complete lifecycle
    of a security investigation.
    """

    workflow_id: str

    event: str

    state: str = "created"

    playbook: str = "default"

    actions: List[str] = field(
        default_factory=list
    )

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )


    def to_dict(self):

        return {

            "workflow_id":
                self.workflow_id,

            "event":
                self.event,

            "state":
                self.state,

            "playbook":
                self.playbook,

            "actions":
                self.actions,

            "metadata":
                self.metadata

        }