from datetime import datetime
import uuid


class GraphEngine:

    def __init__(self):
        self.nodes = []
        self.relationships = []


    def add_node(
        self,
        node_type,
        name,
        data=None
    ):

        node = {
            "node_id": f"NODE-{uuid.uuid4().hex[:8].upper()}",
            "type": node_type,
            "name": name,
            "data": data or {},
            "created_at": datetime.utcnow().isoformat()
        }

        self.nodes.append(node)

        return node


    def add_relationship(
        self,
        source,
        target,
        relation
    ):

        relationship = {
            "relationship_id":
                f"REL-{uuid.uuid4().hex[:8].upper()}",

            "source": source,
            "target": target,
            "relation": relation,
            "created_at":
                datetime.utcnow().isoformat()
        }

        self.relationships.append(
            relationship
        )

        return relationship


    def get_graph(self):

        return {

            "nodes": self.nodes,

            "relationships":
                self.relationships,

            "node_count":
                len(self.nodes),

            "relationship_count":
                len(self.relationships)

        }