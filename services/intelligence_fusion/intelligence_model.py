from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class IntelligenceModel:
    """
    Unified intelligence object.

    This model is the contract between:
    - Knowledge Graph
    - Threat Intelligence
    - Investigation Runtime
    - Memory Systems
    - Decision Engine
    """

    event: str

    entities: List[str] = field(
        default_factory=list
    )

    relationships: List[Dict[str, Any]] = field(
        default_factory=list
    )

    threats: List[Dict[str, Any]] = field(
        default_factory=list
    )

    confidence: float = 0.0

    risk_score: int = 0

    classification: str = "unknown"

    recommendations: List[str] = field(
        default_factory=list
    )


    def add_entity(
        self,
        entity: str
    ):
        if entity not in self.entities:
            self.entities.append(entity)


    def add_relationship(
        self,
        source: str,
        relation: str,
        target: str
    ):
        self.relationships.append(
            {
                "source": source,
                "relation": relation,
                "target": target
            }
        )


    def add_threat(
        self,
        name: str,
        severity: str
    ):
        self.threats.append(
            {
                "name": name,
                "severity": severity
            }
        )


    def add_recommendation(
        self,
        recommendation: str
    ):
        self.recommendations.append(
            recommendation
        )


    def to_dict(self):
        return {
            "event": self.event,
            "entities": self.entities,
            "relationships": self.relationships,
            "threats": self.threats,
            "confidence": self.confidence,
            "risk_score": self.risk_score,
            "classification": self.classification,
            "recommendations": self.recommendations
        }