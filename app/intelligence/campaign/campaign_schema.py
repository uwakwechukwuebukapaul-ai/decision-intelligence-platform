"""
Sentinel DNA - Campaign Intelligence Schema
"""


from dataclasses import dataclass, field
from datetime import datetime




@dataclass
class CampaignResult:

    campaign_id: str

    indicators: list[str]

    confidence: int

    techniques: list[dict]

    reasoning: list[str] = field(
        default_factory=list
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )

