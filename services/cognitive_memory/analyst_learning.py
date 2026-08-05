from datetime import datetime


class AnalystLearning:

    def __init__(self):
        self.learning_events = []

    def record_learning(self, lesson):
        event = {
            "lesson": lesson,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.learning_events.append(event)

        return event

    def get_lessons(self):
        return self.learning_events

    def improve_pattern(self, pattern):
        return {
            "pattern": pattern,
            "status": "learning_updated"
        }