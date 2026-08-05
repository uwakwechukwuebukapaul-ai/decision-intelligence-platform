class NodeManager:
    """
    Manages intelligence graph nodes.

    Handles:
    - node creation
    - node validation
    - node lookup
    """

    def __init__(self):
        self.nodes = []


    def create(self, node_type, value):

        node = {
            "type": node_type,
            "value": value
        }

        self.nodes.append(node)

        return node


    def validate(self, node):

        return isinstance(node, dict) and "type" in node


    def find(self, value):

        for node in self.nodes:
            if node.get("value") == value:
                return node

        return None


    def list_nodes(self):

        return self.nodes