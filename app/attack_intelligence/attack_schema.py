from dataclasses import dataclass
from datetime import datetime


@dataclass
class AttackPath:

    attack_path_id: str
    source: str
    target: str
    risk_level: str
    blast_radius: str
    created_at: str = datetime.utcnow().isoformat()