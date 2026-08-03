from datetime import datetime


class RelationshipEngine:


    def __init__(self):
        self.relationships = []


    def connect(self, source, target, relationship):

        edge = {
            "source": source,
            "target": target,
            "relationship": relationship,
            "created_at": datetime.utcnow().isoformat()
        }

        self.relationships.append(edge)

        return edge


    def get_relationships(self):

        return self.relationships