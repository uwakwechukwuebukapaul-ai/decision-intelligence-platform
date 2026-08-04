from .graph_store import GraphStore
from .entity_manager import EntityManager
from .relationship_engine import RelationshipEngine
from .graph_query import GraphQuery


class KnowledgeGraphEngine:


    def __init__(self):

        self.store = GraphStore()

        self.entities = EntityManager(
            self.store
        )

        self.relationships = RelationshipEngine(
            self.store
        )

        self.query = GraphQuery(
            self.store
        )


    def add_entity(
        self,
        entity_type,
        name,
        attributes=None
    ):

        if attributes is None:
            attributes = {}


        entity = self.entities.create_entity(
            entity_type,
            name,
            attributes
        )


        self.store.add_entity(
            entity
        )


        return entity



    def add_relationship(
        self,
        source,
        relation,
        target
    ):

        relationship = self.relationships.create_relationship(
            source,
            relation,
            target
        )


        self.store.add_relationship(
            relationship
        )


        return relationship



    def connect(
        self,
        source,
        relation,
        target
    ):

        return self.add_relationship(
            source,
            relation,
            target
        )



    def analyze(
        self,
        event
    ):

        threat = self.add_entity(
            "indicator",
            event,
            {
                "source": "event_analysis"
            }
        )


        technique = self.add_entity(
            "technique",
            "PowerShell"
        )


        self.add_relationship(
            threat["name"],
            "uses",
            technique["name"]
        )


        return {

            "event": event,

            "entities":
                self.store.get_entities(),

            "relationships":
                self.store.get_relationships(),

            "status":
                "knowledge_graph_processed"
        }



    def process(
        self,
        event
    ):

        return self.analyze(
            event
        )