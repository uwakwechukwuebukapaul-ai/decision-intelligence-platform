class ExecutionContext:
    """
    Shared memory object passed between SOC agents.
    """


    def __init__(
        self,
        session
    ):

        self.session = session

        self.data = {}



    def set(
        self,
        key,
        value
    ):

        self.data[key] = value



    def get(
        self,
        key,
        default=None
    ):

        return self.data.get(
            key,
            default
        )



    def export(self):

        return {

            "session":
            self.session.to_dict(),

            "context":
            self.data

        }