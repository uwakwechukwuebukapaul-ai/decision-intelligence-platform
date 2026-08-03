class DecisionMemory:


    def __init__(
        self,
        repository
    ):

        self.repository = repository



    def store(
        self,
        decision
    ):


        return self.repository.save(

            "decision",

            decision

        )



    def history(self):


        return self.repository.get(
            "decision"
        )