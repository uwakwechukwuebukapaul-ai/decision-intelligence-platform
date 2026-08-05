class EntityResolver:

    def resolve(self, entity):

        return {
            "entity": entity,
            "resolved": True
        }

    def normalize(self, entity):

        return str(entity).lower()