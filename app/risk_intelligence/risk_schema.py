from datetime import datetime
from dataclasses import dataclass


@dataclass
class RiskRecord:

    risk_id: str

    score: int

    level: str

    factors: list

    created_at: str = datetime.utcnow().isoformat()