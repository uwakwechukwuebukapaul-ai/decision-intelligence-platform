from dataclasses import dataclass
from datetime import datetime


@dataclass
class Asset:

    asset_id: str
    hostname: str
    asset_type: str
    owner: str
    criticality: str
    created_at: str = datetime.utcnow().isoformat()