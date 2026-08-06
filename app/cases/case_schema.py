"""
Sentinel DNA - Case Schema

Defines investigation case structures.
"""


from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any



@dataclass
class InvestigationCase:
    """
    Core SOC investigation case object.
    """


    case_id: str

    indicator: str

    severity: str = "unknown"

    status: str = "open"

    confidence: int = 0

    assigned_to: str | None = None

    evidence: dict[str, Any] = field(
        default_factory=dict
    )

    timeline: list[dict[str, Any]] = field(
        default_factory=list
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )


    updated_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )



    def to_dict(self) -> dict:

        return {

            "case_id": self.case_id,

            "indicator": self.indicator,

            "severity": self.severity,

            "status": self.status,

            "confidence": self.confidence,

            "assigned_to": self.assigned_to,

            "evidence": self.evidence,

            "timeline": self.timeline,

            "created_at": self.created_at,

            "updated_at": self.updated_at,

        }