from datetime import datetime


class RelationshipBuilder:

    def build(self, entities):

        relationships = []

        names = [
            entity["name"]
            for entity in entities.get("entities", [])
        ]

        if "ransomware" in names and "powershell" in names:

            relationships.append(
                {
                    "source": "Ransomware",
                    "relationship": "uses",
                    "target": "PowerShell"
                }
            )

        if "powershell" in names and "server" in names:

            relationships.append(
                {
                    "source": "PowerShell",
                    "relationship": "targets",
                    "target": "Server"
                }
            )

        return {
            "relationships": relationships,
            "timestamp": datetime.utcnow().isoformat()
        }