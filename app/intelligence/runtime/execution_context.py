"""
Execution Context

Carries runtime execution metadata throughout
the intelligence execution lifecycle.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
import uuid


@dataclass(slots=True)
class ExecutionContext:
    """
    Shared execution context for a runtime job.
    """

    job_id: str
    capability: str
    payload: dict

    execution_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    metadata: dict = field(
        default_factory=dict
    )

    started_at: str = field(
        default_factory=lambda: datetime.now(
            UTC
        ).isoformat()
    )

    def to_dict(self) -> dict:

        return {
            "execution_id": self.execution_id,
            "job_id": self.job_id,
            "capability": self.capability,
            "payload": self.payload,
            "metadata": self.metadata,
            "started_at": self.started_at,
        }