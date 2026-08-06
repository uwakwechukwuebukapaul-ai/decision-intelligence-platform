from dataclasses import dataclass, asdict
from datetime import datetime
import uuid


@dataclass
class ThreatIndicator:
    ioc: str
    ioc_type: str
    threat_level: str
    risk_score: int
    confidence: float
    source: str
    created_at: str = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.utcnow().isoformat()

    def to_dict(self):
        return asdict(self)


@dataclass
class EnrichmentResult:
    ioc: str
    category: str
    tags: list
    reputation: str
    details: dict
    created_at: str = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.utcnow().isoformat()

    def to_dict(self):
        return asdict(self)


@dataclass
class ThreatReport:
    report_id: str
    indicator: dict
    enrichment: dict
    created_at: str = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.utcnow().isoformat()

    def to_dict(self):
        return asdict(self)