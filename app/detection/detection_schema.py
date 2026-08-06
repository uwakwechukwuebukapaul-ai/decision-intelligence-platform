"""
Detection data schemas.
"""


from datetime import datetime
from dataclasses import dataclass, field



@dataclass
class DetectionResult:

    detection_id: str

    indicator: str

    rule_name: str

    severity: str

    confidence: float

    mitre_techniques: list = field(
        default_factory=list
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )