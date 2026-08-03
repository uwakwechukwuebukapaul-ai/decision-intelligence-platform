from datetime import datetime

from .entity_manager import EntityManager
from .relationship_mapper import RelationshipMapper
from .attack_graph_builder import AttackGraphBuilder
from .threat_relationships import ThreatRelationshipManager
from .asset_mapper import AssetMapper
from .campaign_graph import CampaignGraph
from .graph_memory import GraphMemory
from .graph_logger import GraphLogger


class KnowledgeGraphEngine:

    def __init__(self):

        self.entities = EntityManager()
        self.relationships = RelationshipMapper()
        self.attack_graph = AttackGraphBuilder()
        self.threats = ThreatRelationshipManager()
        self.assets = AssetMapper()
        self.campaigns = CampaignGraph()
        self.memory = GraphMemory()
        self.logger = GraphLogger()


    def build(self, event):

        entities = self.entities.extract(event)

        relationships = self.relationships.map(
            entities
        )

        attack_graph = self.attack_graph.build(
            event
        )

        threat_relationships = self.threats.analyze(
            event
        )

        assets = self.assets.map(
            event
        )

        campaign = self.campaigns.track(
            event
        )


        memory = self.memory.store(
            event,
            relationships
        )

        log = self.logger.record(
            event
        )


        return {

            "status": "completed",

            "event": event,

            "entities": entities,

            "relationships": relationships,

            "attack_graph": attack_graph,

            "threat_relationships": threat_relationships,

            "assets": assets,

            "campaign_graph": campaign,

            "memory": memory,

            "log": log,

            "created_at":
                datetime.utcnow().isoformat()

        }