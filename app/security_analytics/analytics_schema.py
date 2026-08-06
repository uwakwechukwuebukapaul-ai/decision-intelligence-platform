from dataclasses import dataclass
from datetime import datetime


@dataclass
class SecurityMetric:

    metric_id: str

    event_type: str

    severity: str

    score: int

    category: str

    created_at: str = datetime.utcnow().isoformat()