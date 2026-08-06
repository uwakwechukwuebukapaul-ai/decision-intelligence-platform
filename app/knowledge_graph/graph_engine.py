from .entity_manager import EntityManager
from .relationship_builder import RelationshipBuilder
from .graph_repository import GraphRepository
from .attack_graph import AttackGraph


class GraphEngine:


    def __init__(self):

        self.entity_manager = EntityManager()

        self.relationship_builder = RelationshipBuilder()

        self.repository = GraphRepository()

        self.attack_graph = AttackGraph()



    def add_entity(
        self,
        name,
        entity_type
    ):

        entity = self.entity_manager.create_entity(
            name,
            entity_type
        )

        self.repository.save_entity(entity)

        return entity



    def create_relationship(
        self,
        source,
        target,
        relationship
    ):

        relation = self.relationship_builder.build(
            source,
            target,
            relationship
        )

        self.repository.save_relationship(
            relation
        )

        return relation



    def analyze_attack_paths(self):

        return self.attack_graph.analyze(
            self.repository.get_relationships()
        )