from dataclasses import dataclass
from datetime import datetime


@dataclass
class CorrelationResult:

    correlation_id: str
    incident_id: str
    entities: list
    relationships: list
    confidence: float
    created_at: str = datetime.utcnow().isoformat()