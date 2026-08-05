class FeedbackEngine:
    """
    Converts operational outcomes
    into learning feedback.
    """


    def __init__(self):

        self.feedback_records = []



    def process(
        self,
        action,
        outcome
    ):

        feedback = {

            "action": action,

            "outcome": outcome,

            "learning_signal":
                "positive"
                if outcome
                else "negative"

        }


        self.feedback_records.append(
            feedback
        )


        return feedback



    def history(
        self
    ):

        return self.feedback_records