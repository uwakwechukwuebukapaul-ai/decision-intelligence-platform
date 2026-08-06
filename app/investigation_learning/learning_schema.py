from dataclasses import dataclass
from datetime import datetime


@dataclass
class LearningRecord:
    learning_id: str
    incident_id: str
    indicator: str
    previous_decision: str
    optimized_decision: str
    confidence: float
    improvement: str
    created_at: str = datetime.utcnow().isoformat()