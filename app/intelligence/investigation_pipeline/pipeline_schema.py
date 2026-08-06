"""
Sentinel DNA - Investigation Pipeline Schema

Defines pipeline execution contracts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any



@dataclass
class InvestigationPipelineResult:
    """
    Final investigation pipeline output.
    """

    indicator: str

    status: str

    confidence: int = 0

    intelligence: dict[str, Any] = field(
        default_factory=dict
    )

    autonomous_result: dict[str, Any] = field(
        default_factory=dict
    )

    case: dict[str, Any] = field(
        default_factory=dict
    )

    copilot: dict[str, Any] = field(
        default_factory=dict
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )



    def to_dict(self):

        return {

            "indicator": self.indicator,

            "status": self.status,

            "confidence": self.confidence,

            "intelligence": self.intelligence,

            "autonomous_result": self.autonomous_result,

            "case": self.case,

            "copilot": self.copilot,

            "created_at": self.created_at,

        }