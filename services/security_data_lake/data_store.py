class DataStore:
    """
    Core security data persistence layer.

    Future expansion:
    - PostgreSQL
    - Elasticsearch
    - OpenSearch
    - Object storage
    - Data warehouse
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


    def get_all(self):

        return self.storage


    def count(self):

        return len(self.storage)