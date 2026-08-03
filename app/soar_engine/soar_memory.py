from datetime import datetime


class SOARMemory:
    """
    Stores automation history and executed actions.
    """


    def __init__(self):

        self.executions = []



    def store(
        self,
        execution
    ):

        record = {

            "execution":
                execution,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.executions.append(record)


        return record



    def history(self):

        return {

            "executions":
                self.executions,

            "count":
                len(self.executions)

        }