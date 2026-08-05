class IntelligenceRegistry:
    """
    Dynamic registry for intelligence capabilities.
    """

    def __init__(self):

        self.engines = {}


    def register(
        self,
        name,
        engine
    ):

        self.engines[name] = engine


    def get(
        self,
        name
    ):

        return self.engines.get(name)


    def list_engines(self):

        return list(self.engines.keys())


    def execute(
        self,
        name,
        *args,
        **kwargs
    ):

        engine = self.get(name)

        if not engine:
            raise ValueError(
                f"Intelligence engine '{name}' not found"
            )


        return engine(
            *args,
            **kwargs
        )



registry = IntelligenceRegistry()