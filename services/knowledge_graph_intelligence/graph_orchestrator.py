from .graph_engine import GraphEngine
from .node_manager import NodeManager
from .relationship_manager import RelationshipManager
from .attack_path_engine import AttackPathEngine
from .entity_intelligence import EntityIntelligence
from .graph_query_engine import GraphQueryEngine


class GraphOrchestrator:
    def __init__(self):
        self.graph = GraphEngine()
        self.nodes = NodeManager()
        self.relationships = RelationshipManager()
        self.attack_paths = AttackPathEngine()
        self.entities = EntityIntelligence()
        self.query = GraphQueryEngine(self.graph)

    def create_entity(self, entity_id, entity_type, metadata=None):

        entity = self.entities.register_entity(
            entity_id,
            entity_type,
            metadata
        )

        self.nodes.create_node(
            entity_id,
            entity_type,
            metadata
        )

        self.graph.add_node(
            entity_id,
            entity
        )

        return entity


    def connect_entities(self, source, target, relationship):

        edge = self.relationships.add_relationship(
            source,
            target,
            relationship
        )

        self.graph.add_edge(
            source,
            target,
            relationship
        )

        return edge


    def investigate_relationships(self, entity):

        return self.relationships.find_related(entity)