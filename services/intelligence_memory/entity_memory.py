import uuid


class EntityMemory:


    def __init__(self, store):

        self.store = store



    def remember(
        self,
        entity_type,
        name,
        context=None
    ):

        entity = {

            "id":
                f"ENTITY-{uuid.uuid4().hex[:8].upper()}",

            "type":
                entity_type,

            "name":
                name,

            "context":
                context or {}

        }


        return self.store.store_entity(entity)