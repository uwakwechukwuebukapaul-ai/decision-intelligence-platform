from .graph_model import GraphRelationship


class RelationshipEngine:
    """
    Builds relationships between intelligence entities.
    """


    def build(
        self,
        entities
    ):

        relationships = []


        for source in entities:

            for target in entities:

                if source.name != target.name:


                    relationships.append(

                        GraphRelationship(

                            source=source.name,

                            target=target.name,

                            relationship="associated_with",

                            confidence=0.8

                        )

                    )


        return relationships