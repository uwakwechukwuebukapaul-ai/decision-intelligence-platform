from .graph_store import GraphStore
from .entity_manager import EntityManager
from .relationship_builder import RelationshipEngine
from .graph_logger import GraphLogger


class KnowledgeGraphEngine:

    """
    Knowledge Graph Engine.

    Responsibilities:
    - Entity creation
    - Relationship creation
    - Event analysis
    - Sentinel Core compatibility processing
    """


    def __init__(self):

        self.store = GraphStore()

        self.entity_manager = EntityManager(
            self.store
        )

        self.relationship_engine = RelationshipEngine(
            self.store
        )

        self.logger = GraphLogger()



    def add_entity(
        self,
        entity_type,
        name,
        attributes=None
    ):

        if attributes is None:
            attributes = {}


        entity = self.entity_manager.create_entity(
            entity_type,
            name,
            attributes
        )


        if hasattr(self.store, "add_entity"):
            self.store.add_entity(entity)

        elif hasattr(self.store, "save_entity"):
            self.store.save_entity(entity)

        elif hasattr(self.store, "add_node"):
            self.store.add_node(entity)


        return entity



    def add_relationship(
        self,
        source,
        relation,
        target
    ):


        relationship = self.relationship_engine.create_relationship(
            source,
            relation,
            target
        )


        return relationship



    def _get_relationships(self):

        if hasattr(self.store, "relationships"):
            return self.store.relationships

        return []



    def analyze(
        self,
        event
    ):

        entities = []

        relationships = self._get_relationships()


        keywords = [

            "ransomware",
            "powershell",
            "malware",
            "phishing",
            "attack"

        ]


        for keyword in keywords:

            if keyword in event.lower():

                entity = self.add_entity(

                    "indicator",

                    keyword,

                    {
                        "source":
                            "event_analysis"
                    }

                )

                entities.append(entity)



        return {


            "event":
                event,


            "entities":
                entities,


            "relationships":
                relationships,


            "status":
                "knowledge_graph_processed"

        }



    def process(
        self,
        event
    ):

        return self.analyze(event)