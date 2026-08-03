from datetime import datetime


class ContextBuilder:
    """
    Creates unified investigation context.
    """

    def build(self, data):

        return {
            "context": {
                "incident": data,
                "entities": [],
                "related_events": [],
                "created_at": datetime.utcnow().isoformat()
            },
            "status": "completed"
        }