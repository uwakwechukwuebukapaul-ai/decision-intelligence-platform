class RelationshipEngine:

    def connect(self, source, target, relationship):

        return {
            "source": source,
            "target": target,
            "relationship": relationship
        }

    def infer(self, graph):

        return []