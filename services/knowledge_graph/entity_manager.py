import uuid


class EntityManager:


    def __init__(self, store):

        self.store = store



    def create_entity(
        self,
        entity_type,
        name,
        attributes
    ):

        entity = {

            "id":
                f"ENTITY-{uuid.uuid4().hex[:8].upper()}",

            "type":
                entity_type,

            "name":
                name,

            "attributes":
                attributes
        }


        self.store.entities.append(entity)


        return entity