class PatternMemory:
    """
    Learns recurring security patterns.

    Examples:
    - attacker behavior
    - malware patterns
    - detection patterns
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