"""
Sentinel DNA - Incident Schema

Standard enterprise incident representation.
"""


from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime





@dataclass
class Incident:

    incident_id: str

    indicator: str

    severity: str

    priority: str

    risk_score: int

    confidence: int

    status: str = "open"

    mitre: list = field(default_factory=list)

    evidence: dict = field(default_factory=dict)

    recommendations: list = field(default_factory=list)

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )



    def to_dict(
        self,
    ) -> dict:

        return {

            "incident_id": self.incident_id,

            "indicator": self.indicator,

            "severity": self.severity,

            "priority": self.priority,

            "risk_score": self.risk_score,

            "confidence": self.confidence,

            "status": self.status,

            "mitre": self.mitre,

            "evidence": self.evidence,

            "recommendations": self.recommendations,

            "created_at": self.created_at,

        }