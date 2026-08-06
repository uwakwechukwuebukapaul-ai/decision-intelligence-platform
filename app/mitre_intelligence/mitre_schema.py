from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class MitreRecord:

    mitre_id: str
    techniques: list
    tactics: list
    indicator: str
    risk_level: str
    confidence: float
    created_at: str


    def to_dict(self):
        return asdict(self)


def timestamp():
    return datetime.utcnow().isoformat()