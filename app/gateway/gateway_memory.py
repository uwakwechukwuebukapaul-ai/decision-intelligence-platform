from datetime import datetime


class GatewayMemory:
    """
    Stores gateway operations.
    """


    def __init__(self):

        self.memory = []


    def store(self, data):

        record = {

            "data":
                data,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.memory.append(record)

        return record



    def recall(self):

        return self.memory