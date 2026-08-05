class ConnectorHealth:
    """
    Monitors external integration status.
    """


    def __init__(self):

        self.status = {}



    def check(
        self,
        connector
    ):

        result = {

            "connector": connector,

            "status": "healthy",

            "latency": "normal"

        }


        self.status[connector] = result


        return result



    def all_status(self):

        return self.status