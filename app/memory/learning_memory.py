class LearningMemory:


    def __init__(
        self,
        repository
    ):

        self.repository = repository



    def store_learning(
        self,
        learning
    ):


        return self.repository.save(

            "learning",

            learning

        )



    def get_learning(self):

        return self.repository.get(
            "learning"
        )