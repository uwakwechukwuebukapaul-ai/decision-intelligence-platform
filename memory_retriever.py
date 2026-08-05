class MemoryRetriever:

    def __init__(self, store):
        self.store = store

    def search(self, keyword):

        results = []

        for item in self.store.all():
            if keyword.lower() in str(item).lower():
                results.append(item)

        return results