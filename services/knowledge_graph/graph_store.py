class GraphStore:

    def __init__(self):

        self.entities = []

        self.relationships = []


    def add_entity(
        self,
        entity
    ):
        """
        Store graph entity.
        """

        self.entities.append(
            entity
        )

        return entity


    def add_relationship(
        self,
        relationship
    ):
        """
        Store graph relationship.
        """

        self.relationships.append(
            relationship
        )

        return relationship


    def get_entities(
        self
    ):
        """
        Retrieve stored entities.
        """

        return self.entities


    def get_relationships(
        self
    ):
        """
        Retrieve stored relationships.
        """

        return self.relationships