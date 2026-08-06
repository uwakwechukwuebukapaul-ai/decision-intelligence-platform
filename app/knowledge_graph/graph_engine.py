from datetime import datetime


class KnowledgeGraphEngine:

    def __init__(self):
        self.entities = {}
        self.relationships = []

    def add_entity(self, entity_type, entity_id, data):

        entity = {
            "id": entity_id,
            "type": entity_type,
            "data": data,
            "created_at": datetime.utcnow().isoformat()
        }

        self.entities[entity_id] = entity

        return entity


    def add_relationship(
        self,
        source,
        relation,
        target
    ):

        relationship = {
            "source": source,
            "relation": relation,
            "target": target,
            "created_at": datetime.utcnow().isoformat()
        }

        self.relationships.append(
            relationship
        )

        return relationship


    def get_entity(self, entity_id):

        return self.entities.get(entity_id)


    def get_relationships(self):

        return self.relationships