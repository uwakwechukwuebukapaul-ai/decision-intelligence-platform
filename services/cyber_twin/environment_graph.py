class EnvironmentGraph:
    """
    Builds relationships between
    assets, users, threats and controls.
    """


    def build(
        self,
        nodes=None,
        relationships=None
    ):

        return {

            "status": "graph_created",

            "nodes": nodes or [],

            "relationships": relationships or []

        }


    def connect(
        self,
        source,
        target,
        relation
    ):

        return {

            "source": source,

            "target": target,

            "relation": relation

        }