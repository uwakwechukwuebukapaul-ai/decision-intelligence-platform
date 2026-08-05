class AttackPathEngine:
    """
    Discovers possible attacker paths.
    """


    def discover(
        self,
        relationships
    ):

        paths = []


        for relation in relationships:

            paths.append(
                {
                    "path":
                    f"{relation['source']} -> "
                    f"{relation['relation']} -> "
                    f"{relation['target']}"
                }
            )


        return paths