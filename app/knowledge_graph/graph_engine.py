from datetime import datetime

from .entity_manager import EntityManager
from .relationship_builder import RelationshipBuilder
from .attack_graph import AttackGraph
from .asset_graph import AssetGraph
from .threat_graph import ThreatGraph
from .graph_query import GraphQuery
from .graph_memory import GraphMemory
from .graph_logger import GraphLogger


class KnowledgeGraphEngine:

    def __init__(self):

        self.entities = EntityManager()
        self.relationships = RelationshipBuilder()
        self.attack = AttackGraph()
        self.assets = AssetGraph()
        self.threats = ThreatGraph()
        self.query = GraphQuery()
        self.memory = GraphMemory()
        self.logger = GraphLogger()


    def analyze(self, event):

        entities = self.entities.extract(event)

        relationships = self.relationships.build(
            entities
        )

        attack_graph = self.attack.analyze(event)

        asset_graph = self.assets.analyze(event)

        threat_graph = self.threats.analyze(event)

        query = self.query.search(event)

        memory = self.memory.store(
            {
                "entities": entities,
                "relationships": relationships
            }
        )

        log = self.logger.log(event)


        return {

            "status": "completed",

            "event": event,

            "entities": entities,

            "relationships": relationships,

            "attack_graph": attack_graph,

            "asset_graph": asset_graph,

            "threat_graph": threat_graph,

            "query": query,

            "memory": memory,

            "log": log,

            "created_at": datetime.utcnow().isoformat()

        }