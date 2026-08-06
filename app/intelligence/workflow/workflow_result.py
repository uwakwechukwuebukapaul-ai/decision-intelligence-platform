from dataclasses import dataclass, field
from typing import Any


@dataclass
class WorkflowResult:
    """
    Result returned after workflow execution.
    """

    workflow_id: str
    state: str
    data: dict[str, Any] = field(
        default_factory=dict
    )
    error: str | None = None


    def success(self) -> bool:
        return self.error is None