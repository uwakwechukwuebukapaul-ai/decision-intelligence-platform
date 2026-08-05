class GraphEngine:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node_id, data=None):
        self.nodes[node_id] = data or {}
        return self.nodes[node_id]

    def add_edge(self, source, target, relationship):
        edge = {
            "source": source,
            "target": target,
            "relationship": relationship
        }

        self.edges.append(edge)
        return edge

    def get_node(self, node_id):
        return self.nodes.get(node_id)

    def get_edges(self):
        return self.edges

    def graph_summary(self):
        return {
            "nodes": len(self.nodes),
            "edges": len(self.edges)
        }