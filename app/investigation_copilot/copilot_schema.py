from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class CopilotRecord:

    copilot_id: str
    incident_id: str
    summary: str
    risk_explanation: list
    attack_story: str
    recommendations: list
    confidence: float
    created_at: str


    def to_dict(self):

        return asdict(self)


def timestamp():

    return datetime.utcnow().isoformat()