from datetime import datetime


class ConversationManager:

    def manage(self, query, context=None):

        return {
            "query": query,
            "context_available": True if context else False,
            "timestamp": datetime.utcnow().isoformat()
        }