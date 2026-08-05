class MemoryRetrieval:
    """
    AI Memory Retrieval Engine.

    Allows agents to recall previous knowledge.
    """


    def __init__(
        self,
        store
    ):

        self.store = store



    def recall(
        self,
        query
    ):

        return self.store.search(
            query
        )



    def context(
        self,
        query
    ):

        memories = self.recall(
            query
        )


        return {

            "query":
                query,

            "memories":
                memories,

            "count":
                len(memories)

        }