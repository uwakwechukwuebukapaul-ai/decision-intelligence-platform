class ContextBuilder:

    def build(self, intelligence):

        return {
            "context": intelligence,
            "enriched": True
        }


    def enrich(self, data):

        return self.build(data)