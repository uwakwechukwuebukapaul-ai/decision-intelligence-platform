from dataclasses import dataclass
from datetime import datetime


@dataclass
class InvestigationRecord:

    investigation_id: str
    incident_id: str
    verdict: str
    confidence: float
    created_at: str = datetime.utcnow().isoformat()