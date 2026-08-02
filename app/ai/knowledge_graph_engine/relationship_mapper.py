from datetime import datetime


class RelationshipMapper:
    """
    Knowledge Relationship Intelligence Layer

    Maps connections between:
    - decisions
    - outcomes
    - strategies
    - lessons
    - patterns
    """


    def __init__(self):

        self.version = "1.0"

        self.relationships = []



    def create_relationship(
        self,
        source,
        target,
        relationship_type
    ):


        relationship = {

            "id":
                len(self.relationships) + 1,


            "source":
                source,


            "target":
                target,


            "relationship":
                relationship_type,


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.relationships.append(
            relationship
        )


        return relationship



    def get_relationships(self):

        return self.relationships



relationship_mapper = RelationshipMapper()