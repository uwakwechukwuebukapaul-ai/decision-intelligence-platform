class ConversationEngine:
    """
    Natural language interaction layer.

    Future integrations:
    - LLM providers
    - local models
    - RAG pipelines
    - analyst memory retrieval
    """

    def process(self, message, context=None):

        response = {
            "query": message,
            "context_available": context is not None,
            "response": (
                "I am analyzing your SOC request. "
                "Additional investigation context will improve accuracy."
            )
        }

        return response