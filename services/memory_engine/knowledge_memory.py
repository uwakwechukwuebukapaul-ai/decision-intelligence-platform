class KnowledgeMemory:
    """
    Sentinel DNA Security Knowledge Memory.

    Stores reusable security intelligence:

    - MITRE ATT&CK techniques
    - threat intelligence
    - security concepts
    - detection knowledge
    - investigation knowledge

    Supports persistent MemoryStore integration.
    """

    def __init__(
        self,
        store=None
    ):

        self.store = store



    def add(
        self,
        knowledge
    ):

        if self.store:

            return self.store.store(
                "knowledge",
                knowledge
            )

        return knowledge



    def query(
        self,
        keyword
    ):

        if self.store:

            return self.store.search(
                keyword
            )

        return []



    def get_techniques(
        self
    ):

        if self.store:

            records = self.store.get_all()

            return [

                item

                for item in records

                if item.get("type") == "knowledge"

                and "technique" in str(
                    item.get("data")
                ).lower()

            ]

        return []



    def all_knowledge(
        self
    ):

        if self.store:

            records = self.store.get_all()

            return [

                item

                for item in records

                if item.get("type") == "knowledge"

            ]

        return []