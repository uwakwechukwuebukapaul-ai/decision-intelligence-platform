from datetime import datetime, timezone


class ConversationMemory:
    """
    Stores analyst interaction context.

    Future expansion:
    - Vector memory
    - Analyst preference learning
    - Investigation history
    """

    def __init__(self):

        self.history = []


    def remember(
        self,
        question,
        response
    ):

        record = {

            "question": question,

            "response": response,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }


        self.history.append(record)

        return record



    def recall(self):

        return self.history