class RelationshipBuilder:


    def __init__(self, graph):

        self.graph = graph


    def link(self, source, relation, target):

        return self.graph.add_relationship(
            source,
            relation,
            target
        )