from .graph_store import GraphStore
from .entity_manager import EntityManager
from .relationship_engine import RelationshipEngine
from .graph_query import GraphQuery


class KnowledgeGraphEngine:

    def __init__(self):
        self.store = GraphStore()
        self.entities = EntityManager(self.store)
        self.relationships = RelationshipEngine(self.store)
        self.query = GraphQuery(self.store)


    def add_entity(self, entity_type, name, attributes=None):

        return self.entities.create_entity(
            entity_type,
            name,
            attributes or {}
        )


    def add_relationship(
        self,
        source,
        relation,
        target
    ):

        return self.relationships.create_relationship(
            source,
            relation,
            target
        )


    def analyze(self, event):

        return {
            "event": event,
            "entities": self.store.entities,
            "relationships": self.store.relationships,
            "status": "knowledge_graph_processed"
        }