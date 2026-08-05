class QueryParser:
    """
    Converts analyst questions into
    investigation intents.
    """

    def parse(
        self,
        query
    ):

        text = query.lower()


        intent = "general_security_query"


        if "investigate" in text:
            intent = "investigation"


        elif "why" in text or "explain" in text:
            intent = "explanation"


        elif "recommend" in text or "action" in text:
            intent = "recommendation"


        elif "similar" in text or "previous" in text:
            intent = "memory_search"


        return {

            "query": query,

            "intent": intent,

            "keywords": [

                word

                for word in text.split()

                if len(word) > 4

            ]

        }