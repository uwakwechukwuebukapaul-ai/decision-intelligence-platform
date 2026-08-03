from datetime import datetime

from .entity_manager import EntityManager
from .relationship_manager import RelationshipManager
from .graph_builder import GraphBuilder
from .context_engine import ContextEngine
from .knowledge_memory import KnowledgeMemory


class KnowledgeGraphEngine:


    def __init__(self):

        self.entities = EntityManager()

        self.relationships = RelationshipManager()

        self.builder = GraphBuilder()

        self.context = ContextEngine()

        self.memory = KnowledgeMemory()



    def analyze(
        self,
        event
    ):

        entity_result = self.entities.extract(
            event
        )

        relationship_result = self.relationships.build(
            entity_result["entities"]
        )


        graph = self.builder.build(
            entity_result["entities"],
            relationship_result["relationships"]
        )


        context = self.context.generate(
            graph
        )


        self.memory.store(
            graph
        )


        return {

            "status":
                "completed",

            "event":
                event,

            "entities":
                entity_result,

            "relationships":
                relationship_result,

            "graph":
                graph,

            "context":
                context,

            "created_at":
                datetime.utcnow().isoformat()

        }