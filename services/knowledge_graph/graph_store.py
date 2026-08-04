class GraphStore:

    """
    In-memory storage layer for Knowledge Graph.

    Stores:
    - entities
    - relationships
    """


    def __init__(self):

        self.entities = []

        self.relationships = []



    def add_entity(
        self,
        entity
    ):

        self.entities.append(
            entity
        )

        return entity



    def add_node(
        self,
        entity
    ):

        return self.add_entity(
            entity
        )



    def get_entities(
        self
    ):

        return self.entities



    def add_relationship(
        self,
        relationship
    ):

        self.relationships.append(
            relationship
        )

        return relationship



    def add_edge(
        self,
        relationship
    ):

        return self.add_relationship(
            relationship
        )



    def get_relationships(
        self
    ):

        return self.relationships