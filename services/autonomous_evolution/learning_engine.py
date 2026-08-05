from datetime import datetime


class LearningEngine:
    """
    Learns from investigations, analyst actions,
    detection outcomes, and system feedback.
    """

    def __init__(self):
        self.learning_events = []

    def record_learning(self, event_type, data):
        event = {
            "type": event_type,
            "data": data,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.learning_events.append(event)
        return event

    def analyze_patterns(self):
        return {
            "total_learning_events": len(self.learning_events),
            "status": "learning_active"
        }

    def get_learning_history(self):
        return self.learning_events