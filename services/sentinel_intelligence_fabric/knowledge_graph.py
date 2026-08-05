class KnowledgeGraph:

    def __init__(self):

        self.nodes = []
        self.relationships = []


    def add(self, context):

        self.nodes.append(
            context
        )


    def connect(self, source, target, relation):

        self.relationships.append(
            {
                "source": source,
                "target": target,
                "relation": relation
            }
        )


    def query(self):

        return {
            "nodes": self.nodes,
            "relationships": self.relationships
        }