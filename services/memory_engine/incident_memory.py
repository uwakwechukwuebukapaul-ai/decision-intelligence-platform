class IncidentMemory:
    """
    Stores previous SOC investigations
    and incident outcomes.
    """


    def __init__(
        self,
        store=None
    ):

        self.store = store



    def remember(
        self,
        incident
    ):

        if self.store:

            return self.store.store(
                "incident",
                incident
            )


        return incident



    def find_similar(
        self,
        keyword
    ):

        if self.store:

            return self.store.search(
                keyword
            )


        return []