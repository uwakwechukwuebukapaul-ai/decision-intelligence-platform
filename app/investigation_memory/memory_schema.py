from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class InvestigationMemory:

    memory_id: str

    incident_id: str

    indicator: str

    decision: str

    priority: str

    confidence: float

    patterns: list = field(default_factory=list)

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )