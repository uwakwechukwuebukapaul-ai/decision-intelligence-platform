class EngineRegistry:
    """
    Central registry for Sentinel DNA intelligence engines.
    """

    def __init__(self):
        self.engines = {}

    def register(self, name, engine):
        self.engines[name] = engine

    def get(self, name):
        return self.engines.get(name)

    def list_engines(self):
        return list(self.engines.keys())

    def status(self):
        return {
            "registered_engines": self.list_engines(),
            "count": len(self.engines)
        }