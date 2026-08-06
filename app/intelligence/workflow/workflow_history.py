from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class WorkflowHistory:

    events: list[dict] = field(
        default_factory=list
    )


    def record(
        self,
        event: str,
        workflow_id: str,
    ):

        self.events.append(
            {
                "event": event,
                "workflow_id": workflow_id,
                "timestamp": datetime.utcnow(),
            }
        )


    def all(self):

        return self.events