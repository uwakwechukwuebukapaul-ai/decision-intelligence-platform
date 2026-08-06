from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class CorrelationRecord:

    correlation_id: str
    incident_id: str
    entities: list
    relationships: list
    risk_score: int
    confidence: float
    created_at: str


    def to_dict(self):
        return asdict(self)


def timestamp():

    return datetime.utcnow().isoformat()