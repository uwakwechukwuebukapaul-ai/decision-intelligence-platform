class GraphReasoner:
    """
    Connects entities inside the security knowledge graph.
    """

    def analyze(self, entities):

        relationships = []

        for entity in entities:
            relationships.append(
                {
                    "entity": entity,
                    "relationships": []
                }
            )

        return {
            "graph_nodes": relationships,
            "connections": len(
                relationships
            )
        }