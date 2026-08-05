class SearchEngine:
    """
    Security intelligence search layer.

    Future expansion:
    - Elasticsearch
    - OpenSearch
    - Vector search
    """

    def search(self, dataset, keyword):

        results = []

        for item in dataset:

            if keyword.lower() in str(item).lower():

                results.append(item)

        return results