"""
Sentinel DNA

IOC Intelligence Fusion Engine

Enterprise intelligence aggregation layer.

Combines:
- IOC classification
- Risk analysis
- Reputation
- Threat context
- Geo context
- MITRE mapping
- Graph relationships
"""

from __future__ import annotations


from app.intelligence.ioc.ioc_service import (
    IOCService,
)


from app.intelligence.ioc.enrichment.reputation_engine import (
    ReputationEngine,
)


from app.intelligence.ioc.enrichment.threat_context import (
    ThreatContextEngine,
)


from app.intelligence.ioc.enrichment.geo_context import (
    GeoContextEngine,
)


from app.intelligence.ioc.mitre.attack_mapper import (
    AttackMapper,
)


from app.intelligence.ioc.graph.entity_graph import (
    EntityGraph,
)


from app.intelligence.ioc.graph.relationship_engine import (
    RelationshipEngine,
)


from app.intelligence.ioc.fusion.fusion_context import (
    FusionContext,
)



class IntelligenceFusion:
    """
    Unified IOC intelligence engine.
    """


    def __init__(
        self,
    ):

        self.ioc_service = IOCService()

        self.reputation = ReputationEngine()

        self.threat_context = ThreatContextEngine()

        self.geo_context = GeoContextEngine()

        self.attack_mapper = AttackMapper()

        self.entity_graph = EntityGraph()

        self.relationship_engine = RelationshipEngine()



    def analyze(
        self,
        indicator: str,
    ) -> dict:
        """
        Generate unified IOC intelligence.
        """


        base = self.ioc_service.analyze(
            indicator
        )


        context = FusionContext(

            indicator=indicator,

            indicator_type=base.get(
                "type",
                "unknown",
            ),

            risk=base.get(
                "risk",
                {},
            ),

        )


        context.reputation = self.reputation.analyze(
            base
        )


        context.threat_context = self.threat_context.analyze(
            base
        )


        context.geo_context = self.geo_context.analyze(
            base
        )


        context.mitre_mapping = self.attack_mapper.map(
            base
        )


        entity = self.entity_graph.create_entity(
            base
        )


        context.relationships = self.relationship_engine.find_relationships(
            entity
        )


        return context.to_dict()