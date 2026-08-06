from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Detection:

    detection_id: str
    indicator: str
    rule: str
    severity: str
    confidence: float
    status: str
    created_at: str


    def to_dict(self):
        return asdict(self)


def timestamp():
    return datetime.utcnow().isoformat()