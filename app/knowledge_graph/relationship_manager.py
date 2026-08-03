from datetime import datetime


class RelationshipManager:

    def __init__(self):

        self.relationships = []


    def build(self, entities):

        created = []

        for index in range(len(entities)-1):

            relationship = {
                "source": entities[index]["name"],
                "target": entities[index+1]["name"],
                "relationship": "associated_with",
                "created_at": datetime.utcnow().isoformat()
            }

            self.relationships.append(
                relationship
            )

            created.append(
                relationship
            )


        return {
            "relationships": created,
            "count": len(created)
        }


    def get_relationships(self):

        return self.relationships