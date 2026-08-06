"""
Sentinel DNA - Reasoning Schema

Defines AI reasoning output structures.
"""


from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any



@dataclass
class ReasoningResult:
    """
    Final AI analyst reasoning result.
    """

    indicator: str

    hypothesis: str

    confidence: int

    severity: str

    analyst_summary: str

    recommended_actions: list[str] = field(
        default_factory=list
    )

    evidence: dict[str, Any] = field(
        default_factory=dict
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )


    def to_dict(self):

        return {

            "indicator": self.indicator,

            "hypothesis": self.hypothesis,

            "confidence": self.confidence,

            "severity": self.severity,

            "analyst_summary":
                self.analyst_summary,

            "recommended_actions":
                self.recommended_actions,

            "evidence":
                self.evidence,

            "created_at":
                self.created_at,
        }