class DataStore:
    """
    Core security data persistence layer.
    """

    def __init__(self):

        self.storage = []


    def save(self, data):

        record = {
            "id": len(self.storage) + 1,
            "data": data
        }

        self.storage.append(record)

        return record


    def all(self):

        return self.storage