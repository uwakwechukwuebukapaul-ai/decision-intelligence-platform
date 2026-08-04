from datetime import datetime


class GraphQuery:

    def search(self, query):

        return {
            "query": query,
            "results": [
                "Related Threat Entity",
                "Related Asset",
                "Related Attack Technique"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }