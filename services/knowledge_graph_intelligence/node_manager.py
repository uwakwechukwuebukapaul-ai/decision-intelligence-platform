class NodeManager:
    def __init__(self):
        self.nodes = {}

    def create_node(self, node_id, node_type, attributes=None):
        node = {
            "id": node_id,
            "type": node_type,
            "attributes": attributes or {}
        }

        self.nodes[node_id] = node
        return node

    def get_node(self, node_id):
        return self.nodes.get(node_id)

    def update_node(self, node_id, attributes):
        if node_id in self.nodes:
            self.nodes[node_id]["attributes"].update(attributes)

        return self.nodes.get(node_id)

    def list_nodes(self):
        return list(self.nodes.values())