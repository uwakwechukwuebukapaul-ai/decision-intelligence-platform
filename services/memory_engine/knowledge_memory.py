class KnowledgeMemory:
    """
    Security knowledge memory.

    Stores MITRE techniques,
    threat intelligence,
    and security concepts.
    """


    def __init__(
        self,
        store=None
    ):

        self.store = store



    def add(
        self,
        knowledge
    ):

        if self.store:

            return self.store.store(
                "knowledge",
                knowledge
            )


        return knowledge



    def query(
        self,
        keyword
    ):

        if self.store:

            return self.store.search(
                keyword
            )


        return []