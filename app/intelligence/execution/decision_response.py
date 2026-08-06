"""
Decision Response

Returned by the execution pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(slots=True)
class DecisionResponse:

    success: bool

    capability: str

    result: dict = field(default_factory=dict)

    executed_at: str = field(
        default_factory=lambda: datetime.now(
            UTC
        ).isoformat()
    )

    def to_dict(self) -> dict:

        return {
            "success": self.success,
            "capability": self.capability,
            "result": self.result,
            "executed_at": self.executed_at,
        }