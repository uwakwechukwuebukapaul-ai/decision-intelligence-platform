"""
Sentinel DNA Investigation Memory Schema
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class InvestigationMemoryRecord:

    indicator: str

    risk_score: int

    severity: str

    decision: str

    confidence: int

    mitre_mapping: list = field(
        default_factory=list
    )

    evidence: dict = field(
        default_factory=dict
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )


    def to_dict(self):

        return {

            "indicator": self.indicator,

            "risk_score": self.risk_score,

            "severity": self.severity,

            "decision": self.decision,

            "confidence": self.confidence,

            "mitre_mapping": self.mitre_mapping,

            "evidence": self.evidence,

            "created_at": self.created_at,

        }