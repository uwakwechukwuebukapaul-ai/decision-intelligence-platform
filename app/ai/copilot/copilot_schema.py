"""
Sentinel DNA Copilot Schema
"""


from dataclasses import dataclass, field
from datetime import datetime



@dataclass
class CopilotResponse:

    indicator: str

    answer: str

    confidence: int

    recommendations: list[str] = field(
        default_factory=list
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )


    def to_dict(self):

        return {

            "indicator":
                self.indicator,

            "answer":
                self.answer,

            "confidence":
                self.confidence,

            "recommendations":
                self.recommendations,

            "created_at":
                self.created_at,

        }