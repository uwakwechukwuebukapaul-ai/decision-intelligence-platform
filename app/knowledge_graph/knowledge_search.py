class KnowledgeSearch:


    def search(
        self,
        query,
        entities
    ):

        results = []

        for entity in entities:

            if query.lower() in entity["name"].lower():

                results.append(entity)


        return {

            "query": query,

            "results": results,

            "count": len(results)

        }