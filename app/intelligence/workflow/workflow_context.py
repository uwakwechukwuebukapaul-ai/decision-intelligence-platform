from dataclasses import dataclass, field
from typing import Any


@dataclass
class WorkflowContext:
    """
    Runtime context for workflow execution.
    """

    workflow_id: str
    metadata: dict[str, Any] = field(default_factory=dict)
    inputs: dict[str, Any] = field(default_factory=dict)
    outputs: dict[str, Any] = field(default_factory=dict)

    def set_output(
        self,
        key: str,
        value: Any,
    ) -> None:
        self.outputs[key] = value

    def get_output(
        self,
        key: str,
        default=None,
    ):
        return self.outputs.get(key, default)