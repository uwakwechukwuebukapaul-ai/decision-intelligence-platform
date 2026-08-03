from datetime import datetime


class ContextBuilder:

    def build(self, event):

        return {
            "event": event,
            "sources": [
                "Detection Intelligence",
                "Threat Intelligence",
                "Threat Hunting",
                "Knowledge Graph",
                "Incident Response"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }