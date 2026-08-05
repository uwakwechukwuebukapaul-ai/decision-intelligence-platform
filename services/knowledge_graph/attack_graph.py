class AttackGraphEngine:
    """
    Sentinel DNA attack path reasoning engine.

    Maps:

    Threat Actor
        |
    Technique
        |
    Target
        |
    Impact
    """


    def build_attack_path(
        self,
        entities,
        relationships
    ):


        nodes = []


        for entity in entities:

            nodes.append(

                {

                    "node":
                        entity.name,

                    "type":
                        entity.entity_type

                }

            )


        edges = []


        for relationship in relationships:

            edges.append(

                {

                    "from":
                        relationship.source,


                    "to":
                        relationship.target,


                    "relationship":
                        relationship.relationship

                }

            )


        return {

            "nodes":
                nodes,


            "edges":
                edges,


            "status":
                "attack_graph_generated"

        }