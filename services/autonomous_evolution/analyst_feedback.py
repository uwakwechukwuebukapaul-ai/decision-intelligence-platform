from datetime import datetime


class AnalystFeedback:
    """
    Captures SOC analyst feedback for continuous improvement.
    """

    def __init__(self):
        self.feedback = []

    def submit_feedback(self, analyst, category, message):
        item = {
            "analyst": analyst,
            "category": category,
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.feedback.append(item)

        return item

    def get_feedback(self):
        return self.feedback

    def analyze_feedback(self):
        return {
            "feedback_count": len(self.feedback),
            "learning_signal": "available"
        }