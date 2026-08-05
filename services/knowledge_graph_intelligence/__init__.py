from .graph_engine import GraphEngine
from .node_manager import NodeManager
from .relationship_manager import RelationshipManager
from .attack_path_engine import AttackPathEngine
from .entity_intelligence import EntityIntelligence
from .graph_query_engine import GraphQueryEngine
from .graph_orchestrator import GraphOrchestrator


class KnowledgeGraphIntelligence:
    """
    Sentinel DNA Knowledge Graph Intelligence Layer

    Responsible for:
    - Security entity relationships
    - IOC intelligence mapping
    - Attack path reasoning
    - Threat relationship discovery
    - Investigation context expansion
    """

    def __init__(self):
        self.graph_engine = GraphEngine()
        self.node_manager = NodeManager(self.graph_engine)
        self.relationship_manager = RelationshipManager(self.graph_engine)
        self.attack_path_engine = AttackPathEngine(self.graph_engine)
        self.entity_intelligence = EntityIntelligence(self.graph_engine)
        self.query_engine = GraphQueryEngine(self.graph_engine)

        self.orchestrator = GraphOrchestrator(
            self.graph_engine,
            self.node_manager,
            self.relationship_manager,
            self.attack_path_engine,
            self.entity_intelligence,
            self.query_engine,
        )

    def build_security_graph(self, data):
        return self.orchestrator.build_graph(data)

    def investigate_entity(self, entity):
        return self.orchestrator.investigate(entity)