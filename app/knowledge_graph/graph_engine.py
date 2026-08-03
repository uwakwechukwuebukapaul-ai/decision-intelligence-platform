from datetime import datetime

from .node_manager import NodeManager
from .relationship_engine import RelationshipEngine
from .entity_resolver import EntityResolver
from .attack_graph import AttackGraph
from .threat_graph import ThreatGraph
from .asset_graph import AssetGraph
from .graph_memory import GraphMemory
from .graph_logger import GraphLogger


class KnowledgeGraphEngine:

    def __init__(self):
        self.nodes = NodeManager()
        self.relationships = RelationshipEngine()
        self.entities = EntityResolver()
        self.attack_graph = AttackGraph()
        self.threat_graph = ThreatGraph()
        self.asset_graph = AssetGraph()
        self.memory = GraphMemory()
        self.logger = GraphLogger()

    def analyze(self, incident):

        entities = self.entities.resolve(incident)

        nodes = self.nodes.create_nodes(
            incident,
            entities
        )

        relationships = self.relationships.create_relationships(
            nodes
        )

        attack_path = self.attack_graph.build(
            incident
        )

        threat_context = self.threat_graph.build(
            incident
        )

        asset_context = self.asset_graph.build(
            incident
        )

        memory = self.memory.store(
            incident,
            relationships
        )

        log = self.logger.log(
            incident
        )

        return {
            "status": "completed",
            "incident": incident,
            "entities": entities,
            "nodes": nodes,
            "relationships": relationships,
            "attack_graph": attack_path,
            "threat_graph": threat_context,
            "asset_graph": asset_context,
            "memory": memory,
            "log": log,
            "created_at": datetime.utcnow().isoformat()
        }