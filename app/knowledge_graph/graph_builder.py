from datetime import datetime


class GraphBuilder:


    def build(
        self,
        entities,
        relationships
    ):

        return {

            "nodes": entities,

            "edges": relationships,

            "graph_type":
                "Security Knowledge Graph",

            "timestamp":
                datetime.utcnow().isoformat()

        }