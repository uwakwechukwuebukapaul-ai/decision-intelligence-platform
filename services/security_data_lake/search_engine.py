class SearchEngine:
    """
    Security data search layer.

    Provides search capability across:
    - events
    - evidence
    - investigations
    - threat artifacts
    """

    def __init__(self):

        self.index = []


    def index_record(self, record):

        self.index.append(record)

        return record


    def search(self, query):

        results = []

        query = str(query).lower()

        for record in self.index:

            if query in str(record).lower():

                results.append(record)

        return results


    def count(self):

        return len(self.index)


    def clear(self):

        self.index = []

        return True