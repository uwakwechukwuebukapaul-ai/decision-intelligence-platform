class GraphNode:
    """
    Represents an investigation entity.

    Examples:
    - User
    - Host
    - IOC
    - Malware
    - Process
    - MITRE Technique
    """

    def __init__(
        self,
        node_id,
        node_type,
        value,
        metadata=None
    ):
        self.node_id = node_id
        self.node_type = node_type
        self.value = value
        self.metadata = metadata or {}

    def to_dict(self):

        return {
            "node_id": self.node_id,
            "node_type": self.node_type,
            "value": self.value,
            "metadata": self.metadata
        }