from datetime import datetime


class RelationshipEngine:

    def create_relationships(self, nodes):

        return {
            "relationships": [
                "Threat Actor -> Malware",
                "Malware -> Technique",
                "Technique -> Asset",
                "Asset -> Incident"
            ],
            "source_nodes": nodes,
            "created_at": datetime.utcnow().isoformat()
        }