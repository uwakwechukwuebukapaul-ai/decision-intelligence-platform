class ResearchMemory:


    def __init__(
        self,
        repository
    ):

        self.repository = repository



    def store(
        self,
        research
    ):


        return self.repository.save(

            "research",

            research

        )



    def history(self):

        return self.repository.get(
            "research"
        )