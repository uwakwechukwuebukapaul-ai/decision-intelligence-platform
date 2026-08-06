"""
Sentinel DNA Intelligence Fusion Schema
"""

from dataclasses import dataclass, field


@dataclass
class FusionResult:

    incident_id: str

    incident: dict

    threat_intelligence: dict = field(
        default_factory=dict
    )

    evidence_count: int = 0

    timeline_count: int = 0

    findings: list = field(
        default_factory=list
    )

    recommendations: list = field(
        default_factory=list
    )

    risk_summary: str = ""