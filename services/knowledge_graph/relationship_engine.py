class RelationshipEngine:
    """
    Creates intelligence relationships
    between security entities.
    """


    def build_relationships(
        self,
        entities
    ):

        relationships = []


        if (
            "ransomware" in entities
            and "powershell" in entities
        ):

            relationships.append(
                {
                    "source": "ransomware",
                    "relation": "uses",
                    "target": "powershell"
                }
            )


        if (
            "powershell" in entities
            and "server" in entities
        ):

            relationships.append(
                {
                    "source": "powershell",
                    "relation": "executes_on",
                    "target": "server"
                }
            )


        return relationships