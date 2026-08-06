"""
Sentinel DNA

IOC Fusion Context

Shared intelligence container.

Purpose:
- Prevent repeated enrichment calls
- Maintain investigation state
- Provide enterprise intelligence object
"""

from __future__ import annotations

from dataclasses import dataclass, field



@dataclass
class FusionContext:
    """
    Unified IOC intelligence context.
    """


    indicator: str


    indicator_type: str = "unknown"


    risk: dict = field(
        default_factory=dict
    )


    reputation: dict = field(
        default_factory=dict
    )


    threat_context: dict = field(
        default_factory=dict
    )


    geo_context: dict = field(
        default_factory=dict
    )


    mitre_mapping: list = field(
        default_factory=list
    )


    relationships: list = field(
        default_factory=list
    )


    def to_dict(
        self,
    ) -> dict:
        """
        Convert intelligence context
        into API response format.
        """


        return {

            "indicator": self.indicator,


            "type": self.indicator_type,


            "risk": self.risk,


            "reputation": self.reputation,


            "threat_context": self.threat_context,


            "geo_context": self.geo_context,


            "mitre_mapping": self.mitre_mapping,


            "relationships": self.relationships,

        }