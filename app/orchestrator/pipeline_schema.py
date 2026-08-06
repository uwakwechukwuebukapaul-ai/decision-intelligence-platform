from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class PipelineResult:
    incident_id: str
    status: str
    stages_completed: list
    intelligence: dict
    decision: dict
    response: dict
    created_at: str = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.utcnow().isoformat()

    def to_dict(self):
        return asdict(self)