from dataclasses import dataclass
from datetime import datetime


@dataclass
class BehaviorEvent:

    event_id: str
    user: str
    activity: str
    risk_score: int
    risk_level: str
    created_at: str = datetime.utcnow().isoformat()