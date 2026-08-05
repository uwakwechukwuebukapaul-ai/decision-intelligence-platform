class QueryGenerator:

    def generate(self, objective):

        return {
            "query": f"SEARCH FOR {objective}"
        }


    def optimize(self, query):

        return query