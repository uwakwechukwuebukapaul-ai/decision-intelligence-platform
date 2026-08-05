class Relationship:
    """
    Represents connections between investigation entities.
    """

    def __init__(
        self,
        source,
        relation,
        target,
        metadata=None
    ):

        self.source = source
        self.relation = relation
        self.target = target
        self.metadata = metadata or {}

    def to_dict(self):

        return {
            "source": self.source,
            "relation": self.relation,
            "target": self.target,
            "metadata": self.metadata
        }