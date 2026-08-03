from datetime import datetime


class RelationshipEngine:
    """
    Creates intelligence relationships between entities.
    """

    def connect(self, entities):

        relationships = []

        entity_names = [
            item["name"]
            for item in entities
        ]

        for source in entity_names:

            for target in entity_names:

                if source != target:

                    relationships.append(
                        {
                            "source": source,
                            "relationship": "associated_with",
                            "target": target
                        }
                    )

        return {
            "relationships": relationships,
            "count": len(relationships),
            "timestamp": datetime.utcnow().isoformat()
        }