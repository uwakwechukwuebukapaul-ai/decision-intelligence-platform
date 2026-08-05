class RelationshipManager:
    def __init__(self):
        self.relationships = []

    def add_relationship(self, source, target, relation):
        relationship = {
            "source": source,
            "target": target,
            "relation": relation
        }

        self.relationships.append(relationship)
        return relationship

    def get_relationships(self):
        return self.relationships

    def find_related(self, entity):
        results = []

        for relationship in self.relationships:
            if (
                relationship["source"] == entity
                or relationship["target"] == entity
            ):
                results.append(relationship)

        return results