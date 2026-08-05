class LearningFeedback:

    def __init__(self):

        self.history = []


    def process(self, feedback):

        self.history.append(
            feedback
        )

        return {
            "status": "stored",
            "feedback_count": len(
                self.history
            )
        }