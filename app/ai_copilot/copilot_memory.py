from datetime import datetime


class CopilotMemory:
    """
    Stores analyst interactions and AI decisions.
    """


    def __init__(self):

        self.history = []


    def store(
        self,
        interaction
    ):

        record = {

            "interaction":
                interaction,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.history.append(record)


        return record



    def get_history(self):

        return {

            "records":
                self.history,

            "count":
                len(self.history)

        }