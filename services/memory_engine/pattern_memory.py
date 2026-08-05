class PatternMemory:
    """
    Sentinel DNA Pattern Memory.

    Learns recurring security patterns.

    Examples:
    - attacker behavior
    - malware patterns
    - detection patterns
    - threat hunting patterns

    Supports:
    - in-memory operation
    - persistent MemoryStore integration
    """

    def __init__(
        self,
        store=None
    ):

        self.store = store



    def learn(
        self,
        pattern
    ):

        if self.store:

            return self.store.store(
                "pattern",
                pattern
            )


        return pattern



    def detect_pattern(
        self,
        keyword
    ):

        if self.store:

            return self.store.search(
                keyword
            )


        return []



    def all_patterns(
        self
    ):

        if self.store:

            memories = self.store.get_all()

            return [

                item

                for item in memories

                if item.get("type") == "pattern"

            ]


        return []