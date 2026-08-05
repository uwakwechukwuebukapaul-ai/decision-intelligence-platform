class EntityIntelligence:
    def __init__(self):
        self.entities = {}

    def register_entity(self, entity_id, entity_type, metadata=None):
        entity = {
            "id": entity_id,
            "type": entity_type,
            "metadata": metadata or {}
        }

        self.entities[entity_id] = entity

        return entity

    def enrich_entity(self, entity_id, data):
        if entity_id in self.entities:
            self.entities[entity_id]["metadata"].update(data)

        return self.entities.get(entity_id)

    def get_entity(self, entity_id):
        return self.entities.get(entity_id)