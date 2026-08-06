from dataclasses import dataclass
from datetime import datetime


@dataclass
class SecurityDecision:

    decision_id: str

    risk_score: int

    risk_level: str

    decision: str

    signals: list

    recommended_actions: list

    confidence: float

    created_at: str = datetime.utcnow().isoformat()