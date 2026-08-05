from .graph_node import GraphNode
from .relationship import Relationship


class InvestigationGraphEngine:
    """
    Core investigation relationship engine.

    Builds attack paths and entity relationships.
    """

    def __init__(self):

        self.nodes = {}
        self.relationships = []


    def add_node(
        self,
        node: GraphNode
    ):

        self.nodes[node.node_id] = node

        return node


    def add_relationship(
        self,
        relationship: Relationship
    ):

        self.relationships.append(
            relationship
        )

        return relationship


    def get_node(
        self,
        node_id
    ):

        return self.nodes.get(node_id)


    def find_relationships(
        self,
        entity_id
    ):

        return [
            r.to_dict()
            for r in self.relationships
            if (
                r.source == entity_id
                or
                r.target == entity_id
            )
        ]


    def export_graph(self):

        return {

            "nodes": [
                node.to_dict()
                for node in self.nodes.values()
            ],

            "relationships": [
                r.to_dict()
                for r in self.relationships
            ]
        }