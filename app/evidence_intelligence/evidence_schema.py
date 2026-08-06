from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Evidence:

    evidence_id: str
    incident_id: str
    evidence_type: str
    source: str
    confidence: float
    created_at: str


    def to_dict(self):
        return asdict(self)


def timestamp():
    return datetime.utcnow().isoformat()