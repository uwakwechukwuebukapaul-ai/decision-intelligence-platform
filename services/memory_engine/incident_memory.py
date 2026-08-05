class IncidentMemory:
    """
    Sentinel DNA Incident Memory.

    Stores previous SOC investigations,
    incident outcomes, and investigation history.

    Supports:
    - Legacy in-memory operation
    - Persistent MemoryStore integration
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



    def all_incidents(
        self
    ):

        if self.store:

            memories = self.store.get_all()

            return [

                item

                for item in memories

                if item.get("type") == "incident"

            ]


        return []