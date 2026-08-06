"""
Execution Context

Provides a standardized execution context shared across the
Decision Intelligence Platform runtime.

The execution context carries immutable request information and
runtime metadata through the intelligence pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from typing import Dict
from typing import Optional
import uuid


@dataclass(slots=True)
class ExecutionContext:
    """
    Represents a single intelligence execution.

    Every intelligence request should create one ExecutionContext
    that flows through:

        API
            ↓
        Control Plane
            ↓
        Governance
            ↓
        Runtime
            ↓
        Agents
            ↓
        Response Builder
    """

    user_id: str

    capability: str

    objective: Optional[str] = None

    execution_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    correlation_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    decision_trace: list[str] = field(
        default_factory=list
    )

    runtime_metrics: Dict[str, Any] = field(
        default_factory=dict
    )

    governance: Dict[str, Any] = field(
        default_factory=dict
    )

    def add_trace(self, message: str) -> None:
        """
        Append a decision trace entry.
        """

        timestamp = datetime.now(
            timezone.utc
        ).isoformat()

        self.decision_trace.append(
            f"{timestamp} | {message}"
        )

    def add_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store execution metadata.
        """

        self.metadata[key] = value

    def add_runtime_metric(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store runtime metrics.
        """

        self.runtime_metrics[key] = value

    def add_governance_result(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store governance evaluation results.
        """

        self.governance[key] = value

    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize the execution context.
        """

        return {
            "execution_id": self.execution_id,
            "correlation_id": self.correlation_id,
            "user_id": self.user_id,
            "capability": self.capability,
            "objective": self.objective,
            "created_at": self.created_at.isoformat(),
            "metadata": self.metadata,
            "decision_trace": self.decision_trace,
            "runtime_metrics": self.runtime_metrics,
            "governance": self.governance,
        }