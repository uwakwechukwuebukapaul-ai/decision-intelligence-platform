"""
Sentinel DNA - Correlation Result Schema
"""


from dataclasses import dataclass, field
from datetime import datetime




@dataclass
class CorrelationResult:
    """
    Investigation correlation output.
    """


    indicator: str

    correlated: bool

    confidence: int

    matches: list = field(
        default_factory=list
    )

    recommendation: str = (
        "Continue investigation"
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )



    def to_dict(self):

        return {

            "indicator": self.indicator,

            "correlated": self.correlated,

            "confidence": self.confidence,

            "matches": self.matches,

            "recommendation": self.recommendation,

            "created_at": self.created_at,

        }