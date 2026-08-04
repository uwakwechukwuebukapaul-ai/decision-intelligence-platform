from .graph_store import GraphStore
from .entity_manager import EntityManager
from .relationship_engine import RelationshipEngine
from .graph_query import GraphQuery


class KnowledgeGraphEngine:


    def __init__(self):

        self.store = GraphStore()

        self.entities = EntityManager()

        self.relationships = RelationshipEngine()

        self.query = GraphQuery()



    def add_entity(
        self,
        entity_type,
        name
    ):

        entity = self.entities.create_entity(
            entity_type,
            name
        )

        self.store.add_node(
            entity["id"],
            entity
        )

        return entity



    def connect(
        self,
        source,
        relation,
        target
    ):

        return self.store.add_relationship(
            source,
            relation,
            target
        )



    def analyze(self,event):

        ransomware = self.add_entity(
            "Threat",
            event
        )


        powershell = self.add_entity(
            "Technique",
            "PowerShell"
        )


        self.connect(
            ransomware["id"],
            "uses",
            powershell["id"]
        )


        return {

            "event": event,

            "nodes":
            self.store.get_nodes(),

            "relationships":
            self.store.get_relationships(),

            "status":
            "knowledge_graph_processed"

        }