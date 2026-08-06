from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class ThreatIntelRecord:
    intel_id: str
    indicator: str
    indicator_type: str
    threat_type: str
    confidence: float
    severity: str
    source: str
    created_at: str

    def to_dict(self):
        return asdict(self)


def create_timestamp():
    return datetime.utcnow().isoformat()