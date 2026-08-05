class MemoryRetriever:

    def __init__(self, memory_store):
        self.memory_store = memory_store

    def retrieve(self, query):

        memories = self.memory_store.all()

        results = []

        for memory in memories:
            if query.lower() in str(memory).lower():
                results.append(memory)

        return results