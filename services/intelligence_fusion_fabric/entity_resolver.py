class EntityResolver:

    def __init__(self):

        self.entities = {}


    def register(self, entity_id, entity):

        self.entities[entity_id] = entity

        return entity


    def resolve(self, entity_id):

        return self.entities.get(entity_id)


    def identify(self, data):

        return {
            "entity": data,
            "resolved": True
        }