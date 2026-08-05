class GraphQueryEngine:
    def __init__(self, graph_engine=None):
        self.graph_engine = graph_engine

    def find_node(self, node_id):
        if not self.graph_engine:
            return None

        return self.graph_engine.get_node(node_id)

    def search_nodes(self, keyword):
        if not self.graph_engine:
            return []

        results = []

        for node_id, data in self.graph_engine.nodes.items():
            if keyword.lower() in str(data).lower():
                results.append(
                    {
                        "id": node_id,
                        "data": data
                    }
                )

        return results

    def relationships(self):
        if not self.graph_engine:
            return []

        return self.graph_engine.get_edges()