"""
Execution Result

Standard runtime execution response.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(slots=True)
class ExecutionResult:
    """
    Standard runtime result object.
    """

    execution_id: str

    success: bool

    status: str

    engine: str

    output: dict = field(
        default_factory=dict
    )

    error: str | None = None

    duration_ms: float = 0.0

    completed_at: str = field(
        default_factory=lambda: datetime.now(
            UTC
        ).isoformat()
    )

    def to_dict(self) -> dict:

        return {

            "execution_id": self.execution_id,

            "success": self.success,

            "status": self.status,

            "engine": self.engine,

            "duration_ms": round(
                self.duration_ms,
                2,
            ),

            "output": self.output,

            "error": self.error,

            "completed_at": self.completed_at,
        }