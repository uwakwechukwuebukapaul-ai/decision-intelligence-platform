from dataclasses import dataclass, field
from typing import Dict, List, Any


@dataclass
class CopilotResponse:
    """
    Standard AI SOC Copilot response contract.
    """

    answer: str

    confidence: float = 0.0

    recommendations: List[str] = field(
        default_factory=list
    )

    reasoning: Dict[str, Any] = field(
        default_factory=dict
    )

    references: List[str] = field(
        default_factory=list
    )


    def to_dict(self):

        return {

            "answer": self.answer,

            "confidence": self.confidence,

            "recommendations": self.recommendations,

            "reasoning": self.reasoning,

            "references": self.references

        }