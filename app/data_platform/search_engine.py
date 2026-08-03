class SearchEngine:
    """
    Security event search engine.
    """


    def search(
        self,
        events,
        keyword
    ):

        results = []


        for event in events:

            if keyword.lower() in str(event).lower():

                results.append(event)



        return {

            "query":
                keyword,

            "results":
                results,

            "count":
                len(results)

        }