from datetime import datetime
import uuid


class NodeManager:

    def __init__(self):
        self.nodes = []


    def create_node(self, name, node_type):

        node = {
            "node_id": f"NODE-{uuid.uuid4().hex[:8].upper()}",
            "name": name,
            "type": node_type,
            "created_at": datetime.utcnow().isoformat()
        }

        self.nodes.append(node)

        return node


    def get_nodes(self):

        return {
            "count": len(self.nodes),
            "nodes": self.nodes
        }