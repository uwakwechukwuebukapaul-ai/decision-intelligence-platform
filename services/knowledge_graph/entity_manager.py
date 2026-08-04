class EntityManager:

    """
    Entity management layer for Knowledge Graph.

    Responsible for:
    - Creating graph entities
    - Assigning identifiers
    - Managing entity metadata
    """


    def __init__(
        self,
        store=None
    ):

        self.store = store

        self.counter = 0



    def create_entity(
        self,
        entity_type,
        name,
        attributes=None
    ):

        if attributes is None:
            attributes = {}


        self.counter += 1


        entity = {

            "id":
                self.counter,

            "type":
                entity_type,

            "name":
                name,

            "attributes":
                attributes

        }


        return entity