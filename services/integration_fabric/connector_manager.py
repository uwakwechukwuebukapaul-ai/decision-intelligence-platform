class ConnectorManager:
    """
    Manages lifecycle of external connectors.
    """

    def __init__(self):
        self.registry = {}

    def register(self, name, connector):
        self.registry[name] = connector

    def remove(self, name):
        return self.registry.pop(name, None)

    def get(self, name):
        return self.registry.get(name)

    def list_connectors(self):
        return list(self.registry.keys())