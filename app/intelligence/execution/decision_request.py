"""
Decision Request

Represents a request entering the
Decision Intelligence execution pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
import uuid


@dataclass(slots=True)
class DecisionRequest:

    capability: str

    payload: dict = field(default_factory=dict)

    request_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    created_at: str = field(
        default_factory=lambda: datetime.now(
            UTC
        ).isoformat()
    )

    def to_dict(self) -> dict:

        return {
            "request_id": self.request_id,
            "capability": self.capability,
            "payload": self.payload,
            "created_at": self.created_at,
        }