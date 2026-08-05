class IntelligenceGraphEngine:

    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, source, target, relationship):
        self.edges.append(
            {
                "source": source,
                "target": target,
                "relationship": relationship
            }
        )

    def summary(self):
        return {
            "nodes": len(self.nodes),
            "relationships": len(self.edges)
        }