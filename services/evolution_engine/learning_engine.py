class LearningEngine:
    """
    Sentinel DNA Continuous Learning Engine.

    Learns from previous security operations,
    analyst feedback and agent outcomes.
    """


    def __init__(self):

        self.learning_history = []


    def learn(
        self,
        experience
    ):

        record = {

            "experience": experience,

            "status": "learned"

        }


        self.learning_history.append(
            record
        )


        return record



    def get_learning_history(
        self
    ):

        return self.learning_history