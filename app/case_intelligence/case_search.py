class CaseSearch:
    """
    AI assisted case searching.
    """

    def __init__(self, repository=None):

        self.repository = repository


    def search(self, keyword):

        if not self.repository:
            return []

        results = []

        for case in self.repository.cases:

            if keyword.lower() in case["title"].lower():
                results.append(case)

        return {
            "keyword": keyword,
            "matches": len(results),
            "results": results
        }