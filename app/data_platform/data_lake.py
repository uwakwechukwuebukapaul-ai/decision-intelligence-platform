from datetime import datetime


class DataLake:
    """
    Enterprise security data repository.
    """


    def __init__(self):

        self.storage = []



    def store(
        self,
        event
    ):

        self.storage.append(event)


        return {

            "stored":
                True,

            "records":
                len(self.storage),

            "repository":
                "Sentinel DNA Security Data Lake",

            "timestamp":
                datetime.utcnow().isoformat()

        }