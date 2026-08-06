from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class WorkflowEvent:
    """
    Workflow lifecycle event.
    """

    event_type: str
    workflow_id: str
    payload: dict[str, Any] | None = None
timestamp: datetime = datetime.now(timezone.utc)